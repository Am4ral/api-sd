import os
import subprocess
import requests


class WhisperAI:

    def __init__(self):
        self.url = "http://whisper:9000/asr"

    def transcribe(self, file_path):
        with open(file_path, "rb") as f:
            files = {"audio_file": f}
            response = requests.post(self.url, files=files)

        print(response)
        return response
