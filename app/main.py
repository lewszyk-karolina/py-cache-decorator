from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = args + tuple(kwargs.items())

        if key in stored_dict:
            print("Getting from cache")
            return stored_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_dict[key] = result
            return result
    return wrapper
