#!/usr/bin/env python3
"""
This module provides functionality to cache web pages using Redis.
"""

import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Counting with decorators how many times a request
        has been made
    """

    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        rd.incr(f"count:{url}")
        cached_html = rd.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rd.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of the URL.
    """
    return requests.get(url).text
