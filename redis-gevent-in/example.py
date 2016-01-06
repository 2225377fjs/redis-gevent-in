# -*- coding: utf-8 -*-
__author__ = 'fjs'



from connection import BlockingConnectionPool
from redis.client import Redis

client = Redis(connection_pool=BlockingConnectionPool(max_connections=2))


client.set("fjs", "fjs")
print client.get("fjs")

client.lpush("nn", 1)
print client.lpop("nn")

