from .Proceso_de_carga.upload_set_of_videos_facade import upload_set_of_videos_facade
from .p2p import p2p
def upload_facade(instructor):

    print("Para comenzar el proceso de carga, elige el curso en el que deseas cargar los videos\n\n")
    selected_course = ''

    if len(instructor.courses) > 0:
        for course in instructor.courses:
            print("Curso 1:", course.title)
            select_course = input("¿Deseas agregar el contenido en el curso ? s/n ")
            selected_course = course
            if select_course == 's':
                break

        set_of_videos = upload_set_of_videos_facade(instructor,selected_course)
        p2p(set_of_videos,selected_course)
    
    else:
        print("Parece que usted no tiene cursos, cree uno y regrese más tarde.\n")