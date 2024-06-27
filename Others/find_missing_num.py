def find_missing_num(a, n):
    x1 = a[0]
    x2 = 1

    for i in range(1, n):
        x1 = x1 ^ a[i]

    for i in range(2, n + 2):
        x2 = x2 ^ i

    return x1 ^ x2

arr = [1, 2, 3, 5]
N = len(arr)

miss = find_missing_num(arr, N)
print(miss)