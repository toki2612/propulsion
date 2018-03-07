def count_repetition(arr):
    counter = {}
    for s in arr:
        if s not in counter.keys():
            counter[s] = 1
        else:
            counter[s] += 1

    return counter


print(count_repetition(['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']))
# {'kerouac': 2, 'fante': 3, 'buk': 2, 'hemingway': 1, 'hornby': 1}
