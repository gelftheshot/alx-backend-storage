#!/usr/bin/env python3
"""
This module provides functionality to cache web pages using Redis.
"""

import redis
import requests
from functools import wraps
from typing import Callable


def counturl(func: Callable) -> Callable:
    """
    Decorator to count the number of times a URL is accessed.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache the content of a URL.
        """
        r = redis.Redis()
        r.incr(f"{url}")
        if r.get(f"cached:{url}"):
            return r.get(f"{url}").decode('utf-8')
        text = func(url)
        r.set(f'{url}', response, 10)
        return text

    return wrapper


@counturl
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of the URL.
    """
    return requests.get(url).text
