from handlers import VoskHandlerFactory
from handlers import VoskHandler

MODEL_PATH='./models/vosk-model-es-0.42'
FILE_PATH='./waves/laura.mp4'

handler: VoskHandler = VoskHandlerFactory.create_handler(MODEL_PATH, FILE_PATH)
if not handler:
    print("No suitable handler found for the given file.")
else:
    transcription = handler.transcribe()
    # print("transcription:", transcription)

print("terminado")