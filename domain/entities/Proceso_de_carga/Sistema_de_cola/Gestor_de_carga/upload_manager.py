from .send_to_P2P_upload_strategy import SendToP2PUploadStrategy
from .send_to_cache_upload_strategy import SendToCacheUploadStrategy

class UploadManager:
    def __init__(self, video, error_id):
        self.video = video
        self.error_id = error_id
        self.uploadStrategy = None

    def setUploadStrategy(self):
        if self.error_id == 0:
            self.uploadStrategy = SendToP2PUploadStrategy()
        else:
            self.uploadStrategy = SendToCacheUploadStrategy()

    def executeUpload(self):
        return self.uploadStrategy.upload_video(self.video)
