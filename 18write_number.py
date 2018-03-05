def write_number(arg):
    digits = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: 'zero'
    }

    teens = {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        15: 'fifteen',
        18: 'eighteen'
    }

    tys = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    if 0 < arg < 10:
        print(digits[arg])
    elif len(str(arg)) == 2:
        if 10 < arg < 20:
            if arg in teens.keys():
                print(teens[arg])
            else:
                print(digits[arg % 10] + 'teen')
        elif arg % 10 == 0:
            if arg in tys.keys():
                print(tys[arg])
            else:
                print(digits[arg // 10] + 'ty')
        else:
            print(tys[10 * (arg // 10)] + '-' + digits[arg % 10])


write_number(42)
write_number(34)
write_number(57)
write_number(89)
write_number(91)

write_number(11) # "eleven"
write_number(2) # "two"
write_number(32) # "thirty-two"
