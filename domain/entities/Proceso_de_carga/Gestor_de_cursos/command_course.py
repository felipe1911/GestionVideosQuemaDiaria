from .add_course_to_db import add_course_to_db
from .update_course_in_db import update_course_in_db

class CommandCourse:
    def __init__(self):
        pass
    
    def insert_course(self, course):
        add_course_to_db(course)

    def update_course(self, original_course,modified_course):
        update_course_in_db(original_course,modified_course)

    def delete_course(self, course):
        # Eliminar el curso de la base de datos
        return None
    
    def get_course(self,course):
        # Eliminar el curso de la base de datos
        return None