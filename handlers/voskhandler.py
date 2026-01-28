
from abc import ABC, abstractmethod
from vosk import Model

class VoskHandler(ABC):
    def __init__(self,path_to_model: str, path_to_file: str):
        super().__init__()
        self._path_to_model = path_to_model
        self._path_to_file = path_to_file
        self._model = Model(model_path=self._path_to_model)
    @abstractmethod
    def transcribe(self) -> str:
        pass
