from .upload_video_facade import upload_video_facade
from .video_factory import VideoFactory
from .Sistema_de_cola.get_videos_to_upload import get_videos_to_upload
def upload_set_of_videos_facade(instructor):
    videos = []

    print("Para comenzar el proceso de carga, elige el curso en el que deseas cargar los videos\n\n")
    selected_course = ''
    for course in instructor.courses:
        print("Curso 1:", course.title)
        selected_course = input("¿Deseas agregar el contenido en el curso ? s/n ")
        if selected_course == 's':
            break
    
    if selected_course != '':
        num_cursos = input('¿Cuántos cursos deseas cargar? Ingresa un número entero del 1 al 5: ')
        for i in range(int(num_cursos)):
            if i > 5:
                break
            id, title, tags, author, url, duration = upload_video_facade(instructor)
            video_object = VideoFactory.create_video(id, title, tags, author, url, duration)
            videos.append(video_object)
    print("")
    
    videos_to_upload = get_videos_to_upload(videos,instructor)
    return videos_to_upload
    

