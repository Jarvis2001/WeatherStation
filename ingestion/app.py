from flask import Flask, request, jsonify
from ingestion import validate_upload
from ingestion.logger import log_event
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'storage/images_raw'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_files():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files["files"]
    metadata = request.form.to_dict()

    if not file or file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not validate_upload(file, metadata):
        return jsonify({"error": "invalid file or metadata"}), 400
    

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    log_event("File uploaded", filename = filename, metadata = metadata)
    return jsonify({"message": "Upload Successful"}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)