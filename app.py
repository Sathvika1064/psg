from flask import Flask, request, jsonify, send_file
from pro import download_audio_wav
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_index_html():
    return send_file('psg.html') 

@app.route('/run_function', methods=['POST'])
def run_function():
    data = request.json
    print("Received Data:", data)
    parameter1 = data['parameter1']
    parameter2 = "output_audio.wav"
    parameter3 = data['parameter3']

    download_audio_wav(parameter1, parameter2, parameter3)

    return jsonify({"result": "Audio downloaded and saved in WAV format successfully."})


if __name__ == '__main__':
    app.run(debug=True)
