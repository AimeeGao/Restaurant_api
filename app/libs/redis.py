from flask import current_app
from redis import StrictRedis
from redis import ConnectionPool


class Redis:
    def __init__(self):
        self.cli = None

    def connect(self):
        pool = ConnectionPool(
            host=current_app.config['REDIS_HOST'],
            port=current_app.config['REDIS_PORT'],
            db=current_app.config['REDIS_DB'],
            password=current_app.config['REDIS_PASSWORD']
        )
        return StrictRedis(connection_pool=pool)

    def get_uid_by_key(self, key):
        return self.connection.get(key).decode('ascii')

    @property
    def connection(self):
        if self.cli:
            return self.cli
        else:
            self.cli = self.connect()
            return self.cli


redis = Redis()

