from .data_load_strategy import DataLoadStrategy
from .print_stats_command import PrintStatsCommand

def interface_visualize_stats(instructor):
    strategy = DataLoadStrategy()
    course_data = strategy.load_data()
    printStatsCommand = PrintStatsCommand(instructor,course_data)
    printStatsCommand.execute()