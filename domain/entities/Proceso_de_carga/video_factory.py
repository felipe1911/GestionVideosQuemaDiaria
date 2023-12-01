from .video import Video

class VideoFactory:
    def create_video(id, title, tags, author, url, duration):
        return Video(id, title, tags, author, url, duration)
        