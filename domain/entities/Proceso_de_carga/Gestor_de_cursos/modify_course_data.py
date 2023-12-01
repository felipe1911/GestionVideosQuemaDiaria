
from .course_factory import CourseFactory

def create_new_modified_course(course,new_title,new_description,new_tags):
    instructor = course.instructor
    course_object = CourseFactory.create_course(new_title, new_description, instructor, new_tags)
    return course_object