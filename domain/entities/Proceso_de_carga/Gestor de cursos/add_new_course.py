from .invoker_command_course import InvokerCommandCourse
from .course_factory import CourseFactory

def add_new_course(title, description, instructor, tags):
    course_object = CourseFactory.create_course(title, description, instructor, tags)
    instructor.courses.append(course_object)
    create_course_invoker = InvokerCommandCourse(1,course_object)
    create_course_invoker.execute_command()