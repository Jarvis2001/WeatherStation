"""Validation utilities for uploaded sensor files and metadata."""

from ingestion.config import ALLOWED_EXTENSIONS


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension.

    Args:
        filename (str): Name of the uploaded file.

    Returns:
        bool: True if the file extension is allowed, False otherwise.
    """
    extension = filename.rsplit(".", 1)[1].lower()
    return "." in filename and extension in ALLOWED_EXTENSIONS


def validate_upload(file, metadata):
    """Validate uploaded file and required metadata fields.

    Args:
        file: The uploaded file object (e.g., from Flask or FastAPI).
        metadata (dict): Metadata dictionary containing sensor details.

    Returns:
        bool: True if file and metadata meet the validation rules.
    """
    if not allowed_file(file.filename):
        return False

    if "sensor_id" not in metadata or "timestamp" not in metadata:
        return False

    return True
