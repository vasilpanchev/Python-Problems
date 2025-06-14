def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{str(key).capitalize()}: {value}")


print_info(name="Alice", age="25", city="New York")
