def solution(cipher, code):
    answer = ''

    index = 0
    for word in cipher:
        index += 1

        if index == code:
            answer += word
            index = 0
    return answer


print(solution("dfjardstddetckdaccccdegk", 4))