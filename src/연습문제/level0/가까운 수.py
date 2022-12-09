def solution(array, n):
    diff = 10000
    num = 0

    array.sort()

    for a in array:
        if diff > abs(n - a):
            diff = abs(n - a)
            num = a

    return num


print(solution([3, 10, 30], 20))
