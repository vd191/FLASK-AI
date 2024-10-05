from flask import Flask
from flask_cors import CORS
from features.whisper.whisper_controller import whisper_controller

app = Flask(__name__)
CORS(app)

# Register the trading controller
app.register_blueprint(whisper_controller)


