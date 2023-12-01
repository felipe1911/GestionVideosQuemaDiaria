from .course_search import CourseSearch
from .comand_query import CommandQuery

class InvokerCommandQuery:
    def __init__(self, command_id, query):
        self.command_id = command_id
        self.query = query
        self.command = CommandQuery()
    
    def execute_command(self):
        if self.command_id == 1:
            self.command.search_courses_by_description(self.query)
        if self.command_id == 2:
            self.command.search_courses_by_tags(self.query)