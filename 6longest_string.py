def longest_string(s1, s2):
    new_arr = []
    longest = []

    for s in s1 + s2:
        if s.isalpha() and s.islower():
            new_arr.append(s)

    new_arr.sort()

    for el in new_arr:
        if el not in longest:
            longest.append(el)

    return ''.join(longest)


a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'
x = 'abcdefghijklmnopqrstuvwxyz'


print(longest_string(a, b))  # abcdefklmopqwxy
print(longest_string(a, x))  # abcdefghijklmnopqrstuvwxyz

