from .stats_printer import StatsPrinter

class PrintStatsCommand:
    def __init__(self, instructor, course_data):
        self.course_data = course_data
        self.id_instructor_print = instructor.id

    def execute(self):
        StatsPrinter.print_stats(self.id_instructor_print,self.course_data)