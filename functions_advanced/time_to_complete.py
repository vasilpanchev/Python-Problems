import time


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)

    return wrapper


@timer
def slow_function():
    time.sleep(2)


slow_function()
