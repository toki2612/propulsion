def net_amount():
    balance = 0
    transactions = []
    # D for deposit
    # W for withdrawal
    while True:
        transaction = input("Your transaction: ")
        if transaction:
            transactions.append(transaction)
            if transaction[0] == 'D':
                balance += int(transaction[2:])
            elif transaction[0] == 'W':
                balance -= int(transaction[2:])
        else:
            break

    print(balance)


net_amount()
