import json
from commands.commands import LoadDataCommand, UpdateJsonCommand

class DataLoadStrategy:
    def load_data(self):
        redis_data = LoadDataCommand("../data/redis_data.json").execute()

        database_data = LoadDataCommand("../data/database_data.json").execute()

        if redis_data == database_data:
            print("Redis data is up to date. Loading from Redis.")
            return LoadRedis(redis_data).load_data()
        else:
            print("Redis data is different from database data. Will be loading from the database.")
            return LoadDB(database_data).load_data()

class LoadRedis(DataLoadStrategy):
    def __init__(self, redis_data):
        self.redis_data = redis_data

    def load_data(self):
        print("Fetching data from Redis.")
        return self.redis_data

class LoadDB(DataLoadStrategy):
    def __init__(self, database_data):
        self.database_data = database_data

    def load_data(self):
        print("Fetching data from the database.")
        data = self.database_data

        update_command = UpdateJsonCommand("../data/redis_data.json", data)
        update_command.execute()

        return data