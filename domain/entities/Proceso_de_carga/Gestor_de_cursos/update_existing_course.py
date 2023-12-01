from .invoker_command_course import InvokerCommandCourse
from .modify_course_data import create_new_modified_course

def update_existing_course(course, new_title,new_description,new_tags):
    modified_course = create_new_modified_course(course,new_title,new_description,new_tags)
    modified_course_invoker = InvokerCommandCourse(2,course, modified_course)
    modified_course_invoker.execute_command()
