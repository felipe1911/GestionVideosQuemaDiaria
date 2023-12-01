from .load_data_command import LoadDataCommand
from .load_redis import LoadRedis
from .load_db import LoadDB

class DataLoadStrategy:
    def load_data(self):
        redis_data = LoadDataCommand("domain\database\database_courses_redis.json").execute()

        database_data = LoadDataCommand("domain\database\database_courses.json").execute()

        if redis_data == database_data:
            print("Redis data is up to date. Loading from Redis.")
            return LoadRedis(redis_data).load_data()
        else:
            print("Redis data is different from database data. Will be loading from the database.")
            return LoadDB(database_data).load_data()