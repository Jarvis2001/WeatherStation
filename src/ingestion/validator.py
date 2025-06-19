"""Validation utilities for uploaded sensor files and metadata."""

from ingestion.config import ALLOWED_EXTENSIONS


def allowed_file(filename):
    """Return True if the file extension is in the allowed list.

    Args:
        filename (str): The name of the uploaded file.

    Returns:
        bool: True if extension is allowed, False otherwise.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_upload(file, metadata):
    """Validate the uploaded file and its metadata fields.

    Args:
        file: A file-like object with a 'filename' attribute.
        metadata (dict): Dictionary expected to contain 'sensor_id' and 'timestamp'.

    Returns:
        bool: True if both the file type and required metadata are valid.
    """
    if not allowed_file(file.filename):
        return False

    if "sensor_id" not in metadata or "timestamp" not in metadata:
        return False

    return True
