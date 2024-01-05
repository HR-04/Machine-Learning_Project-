from flask import Flask, request, jsonify
import util
import os

app = Flask(__name__)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    # Set the current working directory to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    
    # Load saved artifacts
    util.load_saved_artifacts()
    
    # Run the Flask app on port 5000
    app.run(port=5000)
