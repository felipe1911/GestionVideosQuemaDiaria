from Gestor_de_cola.video_queue import VideoQueue
from Gestor_de_errores_y_excepciones.get_videos_error_list import get_videos_error_list
from Notificacion_de_error.error_notification_manager import error_notification_manager
def add_video_set(videos:list,instructor):
    queue = VideoQueue(videos)
    queue.setOrderStrategy()
    ordered_queue = queue.getOrder()
    print(" La carga se llevará a cabo en el siguiente orden: ", [video.title for video in ordered_queue])
    error_list = get_videos_error_list(ordered_queue,instructor)
    print(error_list)
    error_notification_manager(error_list,ordered_queue)