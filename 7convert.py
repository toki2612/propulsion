def convert(arg):
    if type(arg) is int:
        num_arr = []
        for c in sorted(str(arg))[::-1]:
            num_arr.append(c)
        return num_arr

    else:
        "arg is not a number"


print(convert(1248123794))
