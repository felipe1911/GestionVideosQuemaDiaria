import json

class LoadDataCommand:
    def __init__(self, json_file):
        self.json_file = json_file

    def execute(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        return data