import json

class CourseSearch:
    def __init__(self, json_file_path) -> None:
        self.courses = self.load_courses_from_json(json_file_path)

    def load_courses_from_json(self, json_file_path):
        with open(json_file_path, 'r') as data_base_courses:
            return json.load(data_base_courses)
        
    def search_by_description_from_db(self, query):
        results = []
        for course in self.courses:
            if query.lower() in course["description"].lower():
                results.append(course)
        print(f'\n Resultado de búsqueda para: {query}')
        print(results)
        title_key = 'title'
        description_key = 'description'
        for index_course_result, course_result in enumerate(results):
            print(f'\n{index_course_result}) ')
            print(f'Título: {course_result[title_key]}')
            print(f'Descripción: {course_result[description_key]}')
        

    def search_by_tags_from_db(self, tags_query):
        results = []
        for course in self.courses:
            if any(tag.lower() in [t.lower() for t in course["tags"]] for tag in tags_query):
                results.append(course)

        print(f'\n Resultado de búsqueda para: {tags_query}')
        title_key = 'title'
        tags_key = 'tags'
        for index_course_result, course_result in enumerate(results):
                print(f'{index_course_result}) ')
                print(f'Título: {course_result[title_key]}')
                print(f'Tags: {course_result[tags_key]}')
            