from course import Course

class CourseFactory:
    def create_course(self, title, description, goals):
        return Course(title, description, goals)