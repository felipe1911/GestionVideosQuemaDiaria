from .course_search import CourseSearch

class CommandQuery:
    def __init__(self):
        self.course_seacrch = CourseSearch('domain\database\database_courses.json')

    def search_courses_by_description(self,query):
        self.course_seacrch.search_by_description_from_db(query)

    def search_courses_by_tags(self,query):
        self.course_seacrch.search_by_tags_from_db(query)


