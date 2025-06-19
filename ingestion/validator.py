from ingestion.config import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_upload(file, metadata):
    if not allowed_file(file.filename):
        return False
    
    if "sensor_id" not in metadata or "timestamp" not in metadata:
        return False
    
    return True