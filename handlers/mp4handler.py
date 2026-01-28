from handlers import VoskHandler
import os
import subprocess
import json
from vosk import Model, KaldiRecognizer
from static_ffmpeg import add_paths
add_paths()

class MP4Handler(VoskHandler):
    def __init__(self, path_to_model: str, path_to_file: str):
        super().__init__(path_to_model, path_to_file)

    def transcribe(self) -> str:
        # Configuramos FFmpeg para extraer audio en formato PCM 16bit Mono a 16000Hz
        command = [
            'ffmpeg', '-loglevel', 'quiet', '-i', self._path_to_file,
            '-ar', '16000', '-ac', '1', '-f', 's16le', '-'
        ]
        
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        rec = KaldiRecognizer(self._model, 16000)
        
        full_text = ""
        with open("transcription.txt", "w") as f:
            while True:
                # print("Reading audio data...")
                data = process.stdout.read(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    # Extraemos el texto del JSON parcial
                    result = json.loads(rec.Result())
                    f.write(result.get('text', '') + "\n ")
                    # print(f"LEIDO: {result.get('text', '')}")
                    # full_text += result.get('text', '') + " "
        
        # Añadimos el resultado final
        final_result = json.loads(rec.FinalResult())
        full_text += final_result.get('text', '')
        
        return full_text.strip()