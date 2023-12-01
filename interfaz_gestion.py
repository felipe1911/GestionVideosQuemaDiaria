from domain.p2p.p2p_uploader import P2pUploader
from domain.p2p.p2p_downloader import P2pDownloader
from domain.entities.video import Video
from domain.cache.redis_client import RedisClient
from domain.san.san_concector import SanConector


from domain.entities.Proceso_de_carga.Gestor_de_cursos.interface_course_creation import interface_create_course
from domain.entities.Proceso_de_carga.Gestor_de_cursos.interface_course_editing import interface_edit_course
from domain.entities.Buscar_videos.interface_search_videos import interface_search_videos

from domain.entities.instructor import Instructor
from domain.entities.user import User



video_file = Video('absWorkout.mp4')
test_instructor = Instructor(10,'Ana','ana@gmail.com','3123142')
test_user = User(id=1, name="John Doe", email="john@example.com", phone_number=1234567890)


def interfaz_gestion():
    # #Subir archivos
    # uploader = P2pUploader()
    # uploader.upload(video_file)

    # #Conexion con redis
    # redis = RedisClient()
    # redis.check_cache()
    # redis.insert_cache(video_file)    
    # redis.check_cache()

    # #Conexion con SAN
    # san =  SanConector()


    # #Descargar archivos
    # downloader = P2pDownloader()
    # downloader.download(video_file)
    # #Seleccion tipo de usuario

    

    while True:
        option_role = input('\n1. Instructor\n2. Usuario\n3. Moderador\n4. Salir\n Seleccione su rol: ')
        
        #Opcion instructor
        if option_role == '1':
            print('\nBienvenido a la plataforma instructor\n')
            while True:
                option_action = input('1. Agregar Curso \n2. Modificar Curso \n3. Agregar videos a curso \n4. Visualizar Estadísticas \n5. Salir  \n  ¿Qué desea hacer?: ')
                if option_action == '1':
                    interface_create_course(test_instructor)

                if option_action == '2':
                    interface_edit_course(test_instructor)

                if option_action == '3':
                    #load_videos_to_course(course)   
                    pass 
                if option_action == '5':
                    print('\nSesion cerrada\n')
                    break

        #Opción Usuario
        if option_role == '2':
            print('\nBienvenido a la plataforma usuario\n')
            while True:
                option_action = input('1. Buscar videos \n2. Recibir recomendaciones \n3. Salir \n  ¿Qué desea hacer?: ')
                if option_action == '1':
                    interface_search_videos(test_user)
                    pass
                if option_action == '2':
                    #interface_recomendations(test_user)
                    pass
                if option_action == '3':
                    break



        if option_role == '4':
            break
        

    
interfaz_gestion()