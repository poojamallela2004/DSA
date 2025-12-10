def plusOne(arr):
    carry = 1
    for i in range(len(arr)-1, -1,-1):
        new_val = arr[i] + carry
        arr[i] = new_val % 10
        carry = new_val // 10
    if carry:
        arr = [carry] + arr
    return arr
