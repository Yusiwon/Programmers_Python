def solution(food):
    answer = ''

    for i in range(1, len(food)):
        for r in range(int(food[i]/2)):
            answer += str(i)

    reverse = answer[-1::-1]
    answer += '0'
    answer += reverse
    return answer

solution([1, 3, 4, 6])
solution([1, 7, 1, 2])