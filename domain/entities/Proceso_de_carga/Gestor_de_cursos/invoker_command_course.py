from .command_course import CommandCourse

class InvokerCommandCourse:
    def __init__(self, command_id, course, new_course =None):
        self.command_id = command_id
        self.course = course
        self.new_course = new_course
        self.command = CommandCourse()
    
    def execute_command(self):
        if self.command_id == 1:
            self.command.insert_course(self.course)
        if self.command_id == 2:
            self.command.update_course(self.course, self.new_course)
            


