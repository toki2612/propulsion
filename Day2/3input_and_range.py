def input_and_range(n):
    new_list = list(map(lambda n: (n, n*n), range(1, n + 1)))
    new_dict = {}
    for i in new_list:
        new_dict[i[0]] = i[1]
    return new_dict


print(input_and_range(10))

# result
# for n=10:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
