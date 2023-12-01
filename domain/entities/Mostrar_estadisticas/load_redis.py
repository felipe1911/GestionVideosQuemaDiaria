

class LoadRedis():
    def __init__(self, redis_data):
        self.redis_data = redis_data

    def load_data(self):
        print("Fetching data from Redis.")
        return self.redis_data
