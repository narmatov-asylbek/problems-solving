

def intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    elements = []
    
    l1 = l2 = 0

    while l1 < len(arr1) and l2 < len(arr2):
        if arr1[l1] == arr2[l2]:
            if l1 == 0 or arr1[l1 - 1] != arr1[l1]:
                elements.append(arr1[l1])
            l1 += 1
            l2 += 1
        elif arr1[l1] > arr2[l2]:
            l2 += 1
        elif arr1[l1] < arr2[l2]:
            l1 += 1
    return elements