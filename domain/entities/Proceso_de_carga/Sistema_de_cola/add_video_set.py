from Gestor_de_cola.video_queue import VideoQueue
def add_video_set(videos:list):
    queue = VideoQueue(videos)
    queue.setOrderStrategy()
    order = queue.getOrder()
    print ([video.id for video in order])
