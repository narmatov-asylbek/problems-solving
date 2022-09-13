

def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    res = []

    for i in range(len(intervals)):
        if new_interval[1] < intervals[i][0]:
            res.append(new_interval)
            return res + intervals[i:]
        elif new_interval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
    
    intervals.append(new_interval)
    return res