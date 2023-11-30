from command_course import CommandCourse
class InvokerCommandCourse:
    def __init__(self, command_id, course):
        self.command_id = command_id
        self.course = course
        self.command = CommandCourse()
    
    def execute_command(self):
        if self.command_id == 1:
            self.command.insert_course(self.course)
            


