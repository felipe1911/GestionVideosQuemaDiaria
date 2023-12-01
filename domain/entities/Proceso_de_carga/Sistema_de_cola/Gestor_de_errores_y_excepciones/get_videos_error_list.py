from .video_error import VideoError

def get_videos_error_list(videos,instructor):
    error_list = []
    for video in videos:
        video_error = VideoError(video,instructor)
        video_error.setErrorStrategy()
        error_id = video_error.getErrorId()
        error_list.append(error_id)
    return error_list