import os
from redis import Redis


class RedisClient:
    db: Redis

    def __init__(self):
        self.db = Redis.from_url(f"redis://{os.getenv('REDIS_URI')}/0")

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RedisClient, cls).__new__(cls)
        return cls.instance
