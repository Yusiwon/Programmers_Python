def solution(sides):
    answer = 0

    sides.sort()

    if sides[2] < sides[0]+sides[1]:
        return 1
    else :
        return 2


print(solution([1, 2, 3]))