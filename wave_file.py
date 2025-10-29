#!/usr/bin/env python3

import wave
import sys
import logging
from vosk import Model, KaldiRecognizer, SetLogLevel
import json

logging.basicConfig(level=logging.INFO)
# You can set log level to -1 to disable debug messages
SetLogLevel(-1)

wf = wave.open("./waves/test2.wav", "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":

    logging.info(f"Channels: { wf.getnchannels()}")
    logging.info(f"Sample Width: { wf.getsampwidth()}")
    logging.info(f"Compression Type: { wf.getcomptype()}")
    logging.info("Audio file must be WAV format mono PCM.")
    sys.exit(1)

model = Model(model_path='./models/vosk-model-small-es-0.42')

# You can also init model by name or with a folder path
# model = Model(model_name="vosk-model-en-us-0.21")
# model = Model("models/en")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # print(rec.Result())
        pass
    # else:
        # print(rec.PartialResult())
print(json.loads(rec.FinalResult())['text'])
