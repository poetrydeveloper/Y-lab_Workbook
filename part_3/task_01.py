import functools
from typing import Any


def my_remembers(func) -> Any:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper


@my_remembers
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(55444445))
