

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    res = []

    inter = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= inter[1]:
            inter[1] = max(inter[1], interval[1])
        else:
            res.append(inter)
            inter = interval
    res.append(inter)
    return res


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))