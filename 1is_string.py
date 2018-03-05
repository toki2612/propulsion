# def is_string(arg):
#     return type(arg) == str


def is_string(arg):
    return isinstance(arg, str)


print(is_string('hello'))  # True
print(is_string(['hello']))  # False
print(is_string('this is a long sentence'))  # True
print(is_string({'a': 2}))  # False
