"""Flask application for handling file uploads and storing raw sensor images."""

import os

from flask import Flask, jsonify, request
from pydantic import ValidationError
from werkzeug.utils import secure_filename

from database.mongo_ops import WeatherDB, insert_sensor_data
from validation.schemas.weather_sensor_data import WeatherSensorData

app = Flask(__name__)
UPLOAD_FOLDER = "storage/images_raw"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def log_event(event, **kwargs):
    """Log an event with optional keyword arguments (placeholder implementation)."""
    print(f"{event}: {kwargs}")


weather_db = WeatherDB()


def process_and_store_weather_data(payload: dict):
    """Validate and insert weather sensor data into the database.

    Parses and validates the incoming sensor data against the WeatherSensorData schema.
    If validation succeeds, stores the cleaned record using the weather_db interface.
    Otherwise, prints the validation errors.

    Args:
        payload (dict): Raw sensor data payload to be validated and stored.

    Returns:
        None
    """
    try:
        validated = WeatherSensorData(**payload)
        record = validated.dict(exclude_none=True)
        weather_db.insert_sensor_data(record)
        print("Sensor data inserted successfully.")
    except ValidationError as e:
        print("Validation failed:", e)


def validate_and_store(payload: dict):
    """Validate weather sensor data and store it in the database.

    This function attempts to deserialize and validate a weather sensor
    payload using the `WeatherSensorData` model. If validation is successful,
    it inserts the sanitized record into the database and returns the record ID.
    If validation fails, the error is logged and `None` is returned.

    Args:
        payload (dict): A dictionary representing the weather sensor data,
            expected to conform to the WeatherSensorData schema.

    Returns:
        str or None: The inserted record's ID as a string if successful;
            `None` if validation fails.
    """
    try:
        validated = WeatherSensorData(**payload)
        record = validated.dict(exclude_none=True)
        record_id = insert_sensor_data(record)
        print(f"Inserted with ID: {record_id}")
        return record_id
    except ValidationError as e:
        print(f"Validation error: {e}")
        return None


def validate_upload(file, metadata):
    """Check if the uploaded file has a valid extension and required metadata.

    Args:
        file: A file-like object with a 'filename' attribute.
        metadata (dict): Form metadata that must include 'sensor_id' and 'timestamp'.

    Returns:
        bool: True if the upload is valid, else False.
    """
    # Basic validation: check file extension and required metadata fields
    allowed_extensions = {"jpg", "jpeg", "png", "bmp"}
    filename = file.filename.lower()
    if "." not in filename or filename.rsplit(".", 1)[1] not in allowed_extensions:
        return False
    if not metadata.get("sensor_id") or not metadata.get("timestamp"):
        return False
    return True


@app.route("/upload", methods=["POST"])
def upload_files():
    """Handle POST requests to upload a file with sensor metadata.

    Expects:
        - 'file' in request.files
        - Metadata fields like 'sensor_id' and 'timestamp' in request.form

    Returns:
        JSON response with success message or error, along with HTTP status.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["files"]
    metadata = request.form.to_dict()

    if not file or file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not validate_upload(file, metadata):
        return jsonify({"error": "invalid file or metadata"}), 400

    filename = secure_filename(file.filename or "")
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    log_event("File uploaded", filename=filename, metadata=metadata)
    return jsonify({"message": "Upload Successful"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
