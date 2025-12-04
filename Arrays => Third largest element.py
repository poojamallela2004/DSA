def tlargest(arr):
    if len(arr) < 3:
        return -1
    largest = float('-inf')
    slargest = float('-inf')
    tlargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            tlargest = slargest
            slargest = largest
            largest = arr[i]
        elif arr[i] != largest and arr[i] > slargest:
            tlargest = slargest
            slargest = arr[i]
        elif arr[i] != largest and arr[i] != slargest and arr[i] > tlargest:
            tlargest = arr[i]
    if tlargest != float('-inf'):
        return tlargest
    else:
        return -1
