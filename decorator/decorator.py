#Decorator syntax

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs)[:7] == "Invalid":
            return func(*args, **kwargs)
        return func(*args, **kwargs) + "And some sprinkles on top too. "
    return wrapper

@add_sprinkles
def get_ice_cream(flavour):
    if not isinstance(flavour, str):
        return "Invalid Flavour "
    return f"Here's your {flavour.lower()} ice cream! "

print(get_ice_cream(5))
print(get_ice_cream("chocolate"))