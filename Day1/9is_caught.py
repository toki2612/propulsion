def is_caught(s):
    for i in range(len(s)):
        if s[i] == 'C':
            if 'm' in s[i: i + 4]:
                return True
            else:
                return False


print(is_caught('C.....m'))  # False
print(is_caught('C..m'))  # True
print(is_caught('..C..m'))  # True
print(is_caught('...C...m'))  # False
print(is_caught('C.m'))  # True
