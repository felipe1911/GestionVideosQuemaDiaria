import json
from create_course_dictionary import create_course_dictionary
from write_json import write_json

def add_course_to_db(course):
    course_dictionary = create_course_dictionary(course)
    write_json(course_dictionary,'domain\database\database_courses.json')