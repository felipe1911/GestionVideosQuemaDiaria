from .update_existing_course import update_existing_course


def interface_edit_course(instructor):


    print('Estos son sus cursos: \n')
    for i, course in enumerate(instructor.courses):
        print(f'{i+1}. {course.title}')

    selection_course_to_update = input('Ingrese el curso que desea editar: ')

    course_selected_to_update = instructor.courses[int(selection_course_to_update)-1]

    new_title = input('Nuevo título (Enter para mantener el actual): ') or course_selected_to_update.title

    new_description = input('Nueva descripción (Enter para mantener la actual): ') or course_selected_to_update.title

    new_tags = course_selected_to_update.tags
    print("Ingresa máximo 10 categorías u objetivos del curso")
    for i in range(10):
        new_tags.append(input("Ingresa una categoría: "))
        add_new_tag = input("Ingresa 1 si quieres agregar otra categoría, y cualquier otra cosa de lo contrario: ")
        print("")
        if add_new_tag != "1":
            break
    

    update_existing_course(course_selected_to_update, new_title,new_description,new_tags)
    print("Curso agregado con éxito")
