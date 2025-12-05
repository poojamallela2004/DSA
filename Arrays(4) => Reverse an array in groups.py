def reverseInGroups(arr, k):
    left = 0
    while left < len(arr):
        right = min(left + k - 1, len(arr) - 1)
        l = left
        r = right
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        left += k
    return arr
