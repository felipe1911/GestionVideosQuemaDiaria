from .upload_strategy import UploadStrategy
from .create_video_dictionary import create_video_dictionary

class SendToP2PUploadStrategy(UploadStrategy):
    def upload_video(self,video):
        return create_video_dictionary(video)