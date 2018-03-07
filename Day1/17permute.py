def permute(arr):
    permutations = []
    permutations.append([arr[0]])
    for i in range(1, len(arr)):
        new_permutations = []
        for perm in permutations:
            for j in range(len(perm) + 1):
                new_permutations.append(perm[:j] + [arr[i]] + perm[j:])
        permutations = new_permutations
        print(new_permutations)
    return permutations

def wrong_permute(arr):
    permutations = [[arr[0]]]
    for i in range(1, len(arr)):
        permutations = permutations * (i + 1)
        for perm in permutations:
            perm.insert(0, arr[i])
    return permutations

import itertools

def permute_cheat(arr):
    for i in itertools.permutations(arr):
        print(i)


print(permute([1, 2, 3]))
