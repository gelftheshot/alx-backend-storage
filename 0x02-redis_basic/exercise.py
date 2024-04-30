#!/usr/bin/env python3
""" store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and
        flush the instance using flushdb """
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: callable) -> callable:

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: callable) -> callable:
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        self._redis.rpush(outputs, str(method(self, *args, **kwargs)))
        return str(method(self, *args, **kwargs))
    return wrapper
    


class Cache:
    """ class used to create a cache of redis class """

    def __init__(self):
        """ initing the varable of redis class to
            python varables """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ take a data  object and return it's string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ covert the binary type back to it's form """
        if fn and self._redis.exists(key):
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_int(self, key: str) -> str:
        """ convert data back to int """
        try:
            value = int(self._redis.get(key).decode("utf-8"))
        except Exception:
            value = 0
        return value

    def get_str(self, key: str) -> str:
        """ convert data back to str """
        return self._redis.get(key).decode("utf-8")
