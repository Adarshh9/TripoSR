# app.py
import os
from flask import Flask, request, send_file, jsonify
from utils import initialize_model, process_image, run_model
import torch

app = Flask(__name__)

# Parameter
output_dir = "output/"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Initialize model once when the server starts
model = initialize_model()

@app.route('/', methods=['GET'])
def home():
    return 'Hello'

@app.route('/process_image', methods=['POST'])
def process_image_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found in request'}), 400

    image_file = request.files['image']
    image_path = os.path.join(output_dir, "uploaded_image.png")
    image_file.save(image_path)

    # Process image and run the model
    image = process_image(image_path, output_dir)
    run_model(model, image, output_dir)

    # Return the resulting .obj file
    result_file_path = os.path.join(output_dir, f"mesh.obj")
    return send_file(result_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=5000)
