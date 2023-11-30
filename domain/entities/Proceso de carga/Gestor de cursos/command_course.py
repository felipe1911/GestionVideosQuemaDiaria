import add_course_to_db
class CommandCourse:
    def __init__(self):
        pass
    
    def insert_course(self, course):
        add_course_to_db(course)

    def update_course(self, course):
        # Actualizar el curso en la base de datos
        return None

    def delete_course(self, course):
        # Eliminar el curso de la base de datos
        return None
    
    def get_course(self,course):
        # Eliminar el curso de la base de datos
        return None