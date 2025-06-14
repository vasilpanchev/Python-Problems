def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Positional args: {args}")
        print(f"Keyword args: {kwargs}")
        print(func(*args, **kwargs))

    return wrapper


@log_args
def add_sum(a, b):
    return a + b


add_sum(3, b=5)
