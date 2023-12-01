from .course import Course

class CourseFactory:
    def create_course(title, description, instructor, tags):
        return Course(title, description, instructor, tags)
        