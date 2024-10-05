from flask import jsonify
import whisper
import os

model = whisper.load_model("base")


def audio_to_text(request):
    try: 
        if 'audio' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
            
        audio_file = request.files['audio']

        temp_audio_path = os.path.join("/tmp", audio_file.filename)

        audio_file.save(temp_audio_path)

        result = model.transcribe(temp_audio_path, fp16=False)

        os.remove(temp_audio_path)

        print(result['text'])

        return result['text']
    except:
        return False