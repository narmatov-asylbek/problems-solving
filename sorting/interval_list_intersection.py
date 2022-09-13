

def interval_intersection(l1: list[list[int]], l2: list[list[int]]) -> list[list[int]]:
    left, right = 0, 0
    res = []

    while left < len(l1) and right < len(l2):
        if l1[left][0] > l2[right][1]:
            right += 1
        elif l1[left][1] < l2[right][0]:
            left += 1
        else:
            res.append([max(l1[left][0], l2[right][0]), min(l1[left][1], l2[right][1])])
            if l1[left][1] < l2[right][1]:
                left += 1
            else:
                right += 1
    return res

print(interval_intersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(interval_intersection([[1, 3], [5, 9]], []))