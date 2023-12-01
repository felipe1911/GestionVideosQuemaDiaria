from add_new_course import add_new_course
def interface_create_course(instructor):

    title = input("Ingresa el título del curso: ")
    print("")
    description = input("Ingresa la descripción del curso: ")
    print("")
    tags = []
    print("Ingresa máximo 10 categorías u objetivos del curso")
    for i in range(10):
        tags.append(input("Ingresa una categoría: "))
        add_new_tag = input("Ingresa 1 si quieres agregar otra categoría, y cualquier otra cosa de lo contrario: ")
        print("")
        if add_new_tag != "1":
            break
    add_new_course(title, description, instructor, tags)
    print("Curso agregado con éxito")
    
    

