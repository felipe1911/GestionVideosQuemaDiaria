from course import Course

class CourseFactory:
    def create_course(self, title, description, instructor, tags):
        return Course(title, description, instructor, tags)
        