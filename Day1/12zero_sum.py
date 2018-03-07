def zero_sum(arr):
    sums = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == 0:
                sums.append([i, j])

    return sums


print(zero_sum([1, 5, 0, -5, 3, -1]))  # [[0, 5], [1, 3], [2, 2]]
print(zero_sum([1, -1]))  # [[0, 1]]
print(zero_sum([0, 4, 3, 5]))  # [[0, 0]]
