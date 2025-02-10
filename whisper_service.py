import os
import subprocess
import requests


class WhisperAI:

    def __init__(self):
        self.url = "http://localhost:9003/asr?output=json"

    def transcribe(self, file_path):
        with open(file_path, "rb") as f:
            files = {"audio_file": f}
            response = requests.post(self.url, files=files)

        print(response.json())

    # THIS CODE IS FOR LOCAL RUNNING
    # def __init__(self, model, outputFolder):
    #     # Change the model name to change the model used.
    #     # Avaliable Models:
    #     #   tiny
    #     #   base
    #     #   small
    #     #   medium
    #     #   large --> Best results for PT-BR
    #     self.model_name = model
    #     self.outputFolder = outputFolder

    # def transcript(self, filePath, fileName):
    #     cwd = os.getcwd()
    #     outputPath = os.path.join(cwd, 'transcript', fileName)
    #     print()

    #     # Using subprocess to run the model via CLI
    #     subprocess.run(
    #         [
    #             "whisper",
    #             "--language", "en",
    #             "--word_timestamps", "True",
    #             "--model", self.model_name,
    #             "--output_dir", self.outputFolder,
    #             filePath
    #         ]
    #     )

    #     return outputPath
