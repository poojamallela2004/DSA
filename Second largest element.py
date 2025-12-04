def slargest(arr):
    if len(arr) < 2:
        return -1
    largest = float('-inf')
    slargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] != largest and arr[i] > slargest:
            slargest = arr[i]
    if slargest != float('-inf'): 
        return slargest
    return -1
