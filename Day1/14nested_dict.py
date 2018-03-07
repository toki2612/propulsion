def nested_dict(mylist):
    value = {}
    new_dict = {}

    for i in reversed(mylist):
        new_dict = {i: value}
        value = new_dict

    return new_dict


print(nested_dict([1, 2, 3, 4, 5]))

