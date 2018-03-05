def are_same_type(arr):
    t = type(arr[0])
    for el in arr:
        if not isinstance(el, t):
            return False
    return True


print(are_same_type(['hello', 'world', 'long sentence']))  # True
print(are_same_type([1, 2, 9, 10]))  # True
print(are_same_type([['hello'], 'hello', ['bye']]))  # False
print(are_same_type([['hello'], [1, 2, 3], [{'a': 2}]]))  # True
print(are_same_type([['hello'], set('hello')]))  # False

