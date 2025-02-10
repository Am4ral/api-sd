import requests
import json


class Ollama:
    def __init__(self):
        self.ollama_url = "http://ollama:11434/api/generate"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.payload = {
            "model": "llama3",
            "prompt": "Repeat the sentence: ERROR with the prompt.",
            "stream": False
        }

    def generate(self, prompt):
        self.payload["prompt"] = prompt
        try:
            response = requests.post(
                self.ollama_url, headers=self.headers, json=self.payload)

            data = response.json()  # Directly parse JSON
            actual_response = data.get("response", "No response key found.")

            print(actual_response)
            return actual_response

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
