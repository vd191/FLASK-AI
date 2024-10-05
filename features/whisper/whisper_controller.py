from flask import Blueprint, request, jsonify
from features.whisper import transcribe

whisper_controller = Blueprint('whisper', __name__)

@whisper_controller.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        text = transcribe.audio_to_text(request)

        if (text):
            return jsonify({"text": text}), 200
        else:
            return jsonify({"status": "ERROR"}), 400 
    except:
        return jsonify({"status": "ERROR"}), 400 