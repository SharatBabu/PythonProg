from time import perf_counter
from time import sleep

def long_duration_fn():
    for _ in range(100000000):
        pass

def timer(fn):
    def inner():
        start = perf_counter()
        result = fn()
        end = perf_counter()
        print(f"Run time of {fn.__name__} is {end - start} seconds")
        return result

    return inner

long_duration_fn = timer(long_duration_fn)

long_duration_fn()

@timer
def really_long_fn():
    sleep(1)

really_long_fn()