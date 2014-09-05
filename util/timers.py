import time
from functools import wraps

# credit to dave beazley
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return (result, end-start)
    return wrapper
