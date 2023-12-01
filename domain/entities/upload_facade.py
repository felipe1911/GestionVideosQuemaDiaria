from Proceso_de_carga.upload_set_of_videos_facade import upload_set_of_videos_facade
from p2p import p2p
def upload_facade(instructor):
    set_of_videos = upload_set_of_videos_facade(instructor)
    p2p(set_of_videos,'curso_por_ahora')