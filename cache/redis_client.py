class RedisClient:
    def __init__(self) -> None:
        print('Conexión con el cliente Redis')
        self.cache = []
        pass    

    def insert_cache(self,data):
        self.cache.append(data)

    def check_cache(self):
        print(f'Cache redis: {self.cache}')


