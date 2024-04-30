#!/usr/bin/env python3
""" store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and
        flush the instance using flushdb """
import redis
import uuid
from typing import Union


class Cache:
    """ class used to create a cache of redis class """

    def __init__(self):
        """ initing the varable of redis class to
            python varables """
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ take a data  object and return it's string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
