

def merge(arr1: list[int], m: int, arr2: list[int], n: int) -> None:
    right = m + n - 1

    while m > 0 and n > 0:
        if arr1[m - 1] >= arr2[n - 1]:
            arr1[right] = arr1[m - 1]
            m -= 1
        elif arr1[m - 1] < arr2[n - 1]:
            arr1[right] = arr2[n - 1]
            n -= 1
        right -= 1
    
    while n > 0:
        arr1[right] = arr2[n - 1]
        right -= 1
        n -= 1
    