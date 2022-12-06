def solution(k, m, score):
    score.sort()

    result = 0

    for i in range(len(score)//m):
        box = score[-m:]
        del score[-m:]
        result += box[0] * m
    return result

solution(3, 4, [1, 2, 3, 1, 2, 3, 1])
solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])