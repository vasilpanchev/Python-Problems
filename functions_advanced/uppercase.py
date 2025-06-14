def uppercase(func):
    def wrapper(x):
        value = func(x)
        return str(value).upper()
    return wrapper


@uppercase
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))