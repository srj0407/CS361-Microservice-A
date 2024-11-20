from flask import Flask, request, jsonify
import base64
from datetime import datetime

app = Flask(__name__)

# In-memory storage for uploaded images
image_storage = []

@app.route('/uploadImage', methods=['POST'])
def upload_image():
    data = request.get_json()
    try:
        # Validate and store data
        uploader_name = data['uploader_name']
        upload_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        encoded_image = data['image']
        tags = data['tags']

        # Save data
        image_storage.append({
            'uploader_name': uploader_name,
            'upload_date': upload_date,
            'image': encoded_image,
            'tags': tags
        })
        return jsonify({'message': 'Image uploaded successfully!'}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400

@app.route('/returnImage', methods=['GET'])
def return_image():
    requested_tags = request.json.get('taglist', [])
    result = [
        image for image in image_storage
        if any(tag in image['tags'] for tag in requested_tags)
    ]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=False)
