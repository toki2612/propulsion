def is_alphanumeric(arg):
    if isinstance(arg, str):
        return arg.isalnum()
    else:
        return False


print(is_alphanumeric('11'))  # True
print(is_alphanumeric(['hello']))  # False
print(is_alphanumeric('this is a long sentence'))  # False
print(is_alphanumeric({'a': 2}))  # False
print(is_alphanumeric("this is string....!!!"))  # False
