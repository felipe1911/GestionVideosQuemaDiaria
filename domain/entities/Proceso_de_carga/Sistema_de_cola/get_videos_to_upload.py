from Gestor_de_cola.video_queue import VideoQueue
from Gestor_de_errores_y_excepciones.get_videos_error_list import get_videos_error_list
from Notificacion_de_error.error_notification_manager import error_notification_manager
from Gestor_de_carga.get_videos_info_to_send_to_P2P import get_videos_info_to_send_to_P2P

def get_videos_to_upload(videos:list,instructor):
    queue = VideoQueue(videos)
    queue.setOrderStrategy()
    ordered_queue = queue.getOrder()
    print(" La carga se llevará a cabo en el siguiente orden: ", [video.title for video in ordered_queue])
    print("")
    error_list = get_videos_error_list(ordered_queue,instructor)
    error_notification_manager(error_list,ordered_queue)
    videos_to_upload = get_videos_info_to_send_to_P2P(ordered_queue,error_list)
    return videos_to_upload