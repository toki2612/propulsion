def print_dictionary(start, end):
    new_dict = {}
    for i in range(start, end):
        new_dict[i] = i**2

    for k in new_dict.values():
        print(k)


print_dictionary(1, 21)
