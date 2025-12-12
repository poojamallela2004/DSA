def buySellMultiTrans(arr):
    prices = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prices = prices + arr[i] - arr[i-1]
    return prices
