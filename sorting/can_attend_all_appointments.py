

def can_attend(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    print(intervals)

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

print(can_attend([[1,4], [2,5], [7,9]]))