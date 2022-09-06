

def solution(l: list[int], k: int) -> int:
    left, right = 0, len(l) - 1
    result = -1

    while left <= right:
        m = left + (right - left) // 2
        if l[m] == k:
            result = m
            right = m - 1
        elif l[m] < k:
            left += 1
        else:
            right -= 1
    return result


if __name__ == '__main__':
    print(solution([1, 3, 4,  8, 8, 8, 10], 8))