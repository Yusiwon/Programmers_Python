import math


def solution(n):

    for i in range(2, 12):
        now = math.factorial(i)

        if n < now:
            return i-1


print(solution(3628800))