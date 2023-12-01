from abc import ABC, abstractmethod

class UploadStrategy(ABC):
    @abstractmethod
    def upload_video():
        pass