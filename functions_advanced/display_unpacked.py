def display_info(name: str, age: int, city: str):
    print(f"Name: {name.capitalize()}")
    print(f"Age: {age}")
    print(f"City: {city.capitalize()}")


args = ("Bob", 30)
kwargs = {"city": "London"}
display_info(*args, **kwargs)
