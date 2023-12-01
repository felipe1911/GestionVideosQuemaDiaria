import random

def upload_video_facade(instructor):
    id = random.randint(0, 10000)
    title = input("\n\nIngresa el título del video: ")
    tags = []
    print("Ingresa máximo 10 categorías u objetivos del video\n")
    for i in range(10):
        tags.append(input("Ingresa una categoría: "))
        add_new_tag = input("Ingresa 1 si quieres agregar otra categoría, y cualquier otra cosa de lo contrario: \n")
        if add_new_tag != "1":
            break
    author = instructor
    url = input("Ingresa la url del video: \n")
    duration = int(input("¿Cuántos segundos dura el video? Ingresa un valor entero: \n"))

    return id, title, tags, author, url, duration