import time
from time import perf_counter, sleep
from functools import wraps
from typing import Callable, Any


def time_that_bitch(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # Note that timing your code once isn't the most reliable option
        # for timing your code. Look into the timeit module for more accurate
        # timing.
        start_time: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = perf_counter()

        print(f'"{func.__name__}()" took {end_time - start_time:.3f} seconds to execute')
        return result

    return wrapper