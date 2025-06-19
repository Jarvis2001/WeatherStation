"""Configuration settings for the ingestion pipeline.

Defines upload and logging paths, along with allowed file extensions.
"""

UPLOAD_DIR = "storage/images_raw"
LOG_FILE = "logs/system.log"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "json"}
