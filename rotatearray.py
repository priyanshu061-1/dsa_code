def rotate(arr, k):
    n = len(arr)
    temp = [0] * n   # make a list of size n filled with 0

    for i in range(n):
        temp[(i + k) % n] = arr[i]   # place elements at rotated positions

    return temp

arr = [1, 2, 3, 4]
k = 2
print(rotate(arr, k))
