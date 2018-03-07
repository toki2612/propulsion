def square_evens(arg):
    return list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, arg)))


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square_evens(mylist))
