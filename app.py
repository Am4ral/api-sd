import os
import requests
import subprocess
from flask import Flask, request, jsonify
from elevenlabs_service import ElevenLabs
from ollama_service import Ollama
from whisper_service import WhisperAI

app = Flask(__name__)


def process_audio(audio_file_path):
    whisper_service = WhisperAI()
    ollama_service = Ollama()
    elevenlabs_service = ElevenLabs()

    file_name = os.path.basename(audio_file_path).split(".")[0]
    transcript_text = whisper_service.transcribe(audio_file_path)
    ollama_response = ollama_service.generate(transcript_text)
    generated_audio = elevenlabs_service.generate(ollama_response)

    if generated_audio:
        output_audio_path = f"{file_name}_response.ogg"
        with open(output_audio_path, "wb") as audio_file:
            audio_file.write(generated_audio)
        return output_audio_path

    return "Error generating audio"


@app.route("/process-audio", methods=["POST"])
def process_audio_api():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    file_path = os.path.join("uploads", audio_file.filename)
    audio_file.save(file_path)

    result = process_audio(file_path)

    return jsonify({"message": "Audio processed successfully", "output_file": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5545)
