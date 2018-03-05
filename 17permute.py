def permute(arr):
    permutations = []

    if len(arr) == 1:
        permutations.append(arr)
    else:
        permutations * len(arr)
        for i in permutations:
            i = [arr[-1], i]

    return permutations


print(permute([1, 2, 3]))
