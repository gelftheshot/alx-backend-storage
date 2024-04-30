import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def counturl(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(url):
        r.incr(f"count:{url}")
        if r.exists(f"cached:{url}"):
            return r.get(f"cached:{url}").decode('utf-8')
        text = func(url)
        r.setex(f"cached:{url}", 10, text)
        return text

    return wrapper


@counturl
def get_page(url: str) -> str:
    """Retrieve the HTML content of the URL."""
    return requests.get(url).text
