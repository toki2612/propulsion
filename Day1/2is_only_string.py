# def is_string(arg):
#     return type(arg) == str


def is_only_string(arg):
    if isinstance(arg, str):
        return arg.isalpha()
    else:
        return False


print(is_only_string('11'))  # False
print(is_only_string(['hello']))  # ? Please handle this case!! Should return False
print(is_only_string('this is a long sentence'))  # False
print(is_only_string({'a': 2}))  # # ? Please handle this case!! Should return False
