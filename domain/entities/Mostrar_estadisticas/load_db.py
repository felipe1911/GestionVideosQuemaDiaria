
from .update_json_command import UpdateJsonCommand

class LoadDB():
    def __init__(self, database_data):
        self.database_data = database_data

    def load_data(self):
        print("Fetching data from the database.")
        data = self.database_data

        update_command = UpdateJsonCommand("domain\database\database_courses.json", data)
        update_command.execute()

        return data