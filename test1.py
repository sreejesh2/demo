from flask import Flask, render_template, request, jsonify
import requests
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = requests.post('https://b059-34-19-63-47.ngrok-free.app/generate', json={"prompt": prompt})

    if response.status_code == 200:
        image_bytes = response.content
        
        # Encode the image to Base64
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        
        # Create a JSON response with both image and other data
        response_data = {
            "message": "Image generated successfully",
            "image": encoded_image  # This will be a Base64-encoded image string
        }
        
        return jsonify(response_data), 200
    else:
        return jsonify({"error": f"Generation failed: {response.status_code}", "details": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
