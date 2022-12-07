def solution(balls, share):
    answer = 0

    m = 1
    for i in range(balls, (balls-share), -1):
        m *= i
    s = 1
    for i in range(1, share+1):
        s *= i
    return m // s

print(solution(5, 3))