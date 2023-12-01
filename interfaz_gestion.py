from domain.p2p.p2p_uploader import P2pUploader
from domain.p2p.p2p_downloader import P2pDownloader
from domain.entities.video import Video
from domain.cache.redis_client import RedisClient
from domain.san.san_concector import SanConector
from domain.entities.Proceso_de_carga.Gestor_de_cursos 

archivo_video = Video('absWorkout.mp4')


def interfaz_gestion():
    #Subir archivos
    uploader = P2pUploader()
    uploader.upload(archivo_video)


    #Conexion con redis
    redis = RedisClient()
    redis.check_cache()
    redis.insert_cache(archivo_video)
    redis.check_cache()

    #Conexion con SAN
    san =  SanConector()


    #Descargar archivos
    downloader = P2pDownloader()
    downloader.download(archivo_video)

    #Seleccion tipo de usuario

    

    while True:
        option_role = input('1.Instructor\n2.Usuario\n3. Moderador\n  Seleccione su rol: ')
        
        #Opcion instructor
        if option_role == '1':
            print('\nBienvenido a la plataforma instructor')
            while True:
                option_action = input('1.Agregar Curso \n 2.Modificar Curso \n 3. Visualizar Estadísticas  \n 4. Salir  \n  ¿Qué desea hacer?: ')
                if 
                if option_action == '4':
                    print('\nSesion cerrada\n')
                    break
            

    
interfaz_gestion()