def upper_lower_counter():
    sentence = input("Type your sentence: ")
    uppers = 0
    lowers = 0

    for ch in sentence:
        if ch.isalpha():
            if ch.isupper():
                uppers += 1
            else:
                lowers += 1

    return uppers, lowers


print(upper_lower_counter())
