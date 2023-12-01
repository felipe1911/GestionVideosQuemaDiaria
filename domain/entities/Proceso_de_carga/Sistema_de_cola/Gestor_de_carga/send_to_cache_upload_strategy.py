from .upload_strategy import UploadStrategy
from .send_video_to_cache import send_video_to_cache

class SendToCacheUploadStrategy(UploadStrategy):
    def upload_video(self,video):
        send_video_to_cache(video)
        return None