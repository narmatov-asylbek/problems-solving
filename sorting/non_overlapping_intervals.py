


def erase_overlap_intervals(l1: list[list[int]]) -> int:
    l1.sort(key=lambda x: x[0])

    res = 0
    _, end = l1[0]

    for inter in l1[1:]:
        curr_start, curr_end = inter

        if curr_start < end:
            res += 1
            end = min(curr_end, end)
        else:
            end = curr_end
    return res

