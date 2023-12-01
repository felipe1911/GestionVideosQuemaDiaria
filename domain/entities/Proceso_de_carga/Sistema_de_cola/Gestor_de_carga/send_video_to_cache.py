from .create_video_dictionary import create_video_dictionary
from .write_json import write_json
def send_video_to_cache(video):
    video_dictionary = create_video_dictionary(video)
    write_json(video_dictionary,'domain\cache\error_cache.json')