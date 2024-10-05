from flask import Blueprint, request, jsonify
from features.whisper import transcribe
import random

whisper_controller = Blueprint('whisper', __name__)

@whisper_controller.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    print('transcribe_audio')
    try:
        question = request.form['question']
        question_id = request.form['questionId']

        # Get the file from the request
        if 'audio' not in request.files:
            print("No audio file provided")
            return "No audio file provided", 400
        
        audio = request.files['audio'] 

        print(question)
        print(question_id)
        print(audio)

        text = transcribe.audio_to_text(request)

        score = {
            'question': question,
            'questionId': question_id,
            'anwser': text,
            'content': random.randint(1, 90),
            'pronunciation': random.randint(1, 90),
            'fluency': random.randint(1, 90),
            'overall': random.randint(1, 90),
        }
        
        if (score):
            return jsonify(score), 200
        else:
            return jsonify({"status": "ERROR"}), 400 
    except:
        return jsonify({"status": "ERROR"}), 400 