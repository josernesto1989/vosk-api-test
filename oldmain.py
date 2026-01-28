#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import json
from vosk import Model, KaldiRecognizer
import soundfile as sf
import os

# 1. Load the Vosk model (adjust model path as needed)
model_path = "./models/vosk-model-small-es-0.42" 
if not os.path.exists(model_path):
    print(f"Please download the Vosk model and extract it to {model_path}")
    exit(1)
model = Model(model_path)

# 2. Read the Ogg file using soundfile
ogg_file_path = "./waves/test1.ogg"
data, samplerate = sf.read(ogg_file_path, dtype='int16') # Read as 16-bit integers
# soundfile reads stereo by default if the file is stereo, so we need to ensure mono

# If the audio is stereo, convert to mono by taking the first channel
if data.ndim > 1:
    data = data[:, 0]

# Ensure the sample rate matches the model's expected rate (if different, you'll need to resample)
# The Vosk model object has an attribute for expected sample rate.
# For this example, we'll assume the model supports the file's samplerate or you have resampled it.
# Check your specific Vosk model documentation for its required sample rate.
model_sample_rate = samplerate # Or the rate specified by your model

# 3. Initialize the KaldiRecognizer
rec = KaldiRecognizer(model, model_sample_rate)

# 4. Process the audio frames in chunks
print("Processing audio...")
rec.AcceptWaveform(data.tobytes()) # Pass the entire byte data to the recognizer

# 5. Retrieve the final result
result = json.loads(rec.Result())
print(result['text'])
