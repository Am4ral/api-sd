import requests


class ElevenLabs:
    def __init__(self):
        self.whisper_url = "https://api.elevenlabs.io/v1/text-to-speech/:JBFqnCBsd6RMkjVDRZzb"
        self.headers = {
            "Content-Type": "application/json",
            "xi-api-key": "sk_d37efd0530fbcab7049a42395932cf880c33b98b3f42f79d"

        }
        self.payload = {
            "text": "",
            "model_id": "eleven_multilingual_v2"
        }

    def generate(self, prompt):
        self.payload["prompt"] = prompt

        response = requests.post(self.whisper_url, json=self.payload)

        return response
