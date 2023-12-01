def create_video_dictionary(video):
    video_dictionary = {
        'id' : video.id,
        'title' : video.title,
        'tags' : video.tags,
        'author_id' : video.author.id,
        'url': video.url,
        'duration': video.duration,
        'video': video.comments,
        'likes': video.likes,
        'approved': video.approved
    }
    return video_dictionary