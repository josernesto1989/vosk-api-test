from .voskhandler import VoskHandler
from .wavehandler import WaveHandler
import os

class VoskHandlerFactory:
    _extension_to_handler = {
        '.wav': WaveHandler,
    }
    @classmethod
    def create_handler(cls, model_path, file_path):
        _, ext = os.path.splitext(file_path)
        handler_class = cls._extension_to_handler.get(ext.lower(), None)
        if not handler_class:
            return None
        return handler_class(model_path, file_path)