import json

class UpdateJsonCommand:
    def __init__(self, file_path, new_data):
        self.file_path = file_path
        self.new_data = new_data

    def execute(self):
        with open(self.file_path, "w") as file:
            json.dump(self.new_data, file, indent=2)
        print(f"{self.file_path} file updated.")