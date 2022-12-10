def solution(my_string):
    answer = []

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for s in my_string:
        if s in num:
            answer.append(int(s))

    answer = sorted(answer)
    return answer

print(solution("hi12392"))