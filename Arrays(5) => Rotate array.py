def rotateArray(arr, k):
    n = len(arr)
    k = k % n
    rotate(arr, 0, n-k-1)
    rotate(arr, n-k, n-1)
    rotate(arr, 0, n-1)
    return arr

def rotate(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
