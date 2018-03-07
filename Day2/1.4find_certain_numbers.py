def find_numbers_for(min, max):
    found = []
    for i in range(min, max):
        if i % 7 == 0 and i % 5 != 0:
            found.append(i)

    return found


def find_numbers(_min, _max):
    return list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(_min, _max)))


print(find_numbers_for(1, 36))
print(find_numbers(1, 36))
