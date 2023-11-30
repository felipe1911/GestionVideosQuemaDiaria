import json
import create_course_dictionary

def add_course_to_db(course):
    course_dictionary = create_course_dictionary(course)
    json_object = json.dumps(course_dictionary, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)