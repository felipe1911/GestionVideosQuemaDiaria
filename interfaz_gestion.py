from p2p.p2p_uploader import P2pUploader
from p2p.p2p_downloader import P2pDownloader
from domain.entities.video import Video
from cache.redis_client import RedisClient
from san.san_concector import SanConector

archivo_video = Video('absWorkout.mp4')


#Subir archivos
uploader = P2pUploader()
uploader.upload(archivo_video)


#Conexion con redis
redis = RedisClient()

#Conexion con SAN
san =  SanConector()


#Descargar archivos
downloader = P2pDownloader()
downloader.download(archivo_video)