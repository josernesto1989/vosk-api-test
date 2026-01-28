from .voskhandler import VoskHandler
import wave
from vosk import KaldiRecognizer

class WaveHandler(VoskHandler):
    def __init__(self, path_to_model: str, path_to_file: str):
        super().__init__(path_to_model, path_to_file)

    def transcribe(self) -> str:
        
        wf = wave.open(self._path_to_file, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            raise ValueError("Audio file must be WAV format mono PCM.")

        rec = KaldiRecognizer(self._model, wf.getframerate())
        result = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = rec.Result()
                result += res

        final_res = rec.FinalResult()
        result += json.loads(final_res)['text']
        return result
    