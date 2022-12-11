def solution(my_string, num1, num2):
    answer = ''

    first = my_string[num1]
    second = my_string[num2]

    answer += my_string[0 : num1]
    answer += second
    answer += my_string[num1+1 : num2]
    answer += first
    answer += my_string[num2+1 :]
    return answer


print(solution("I love you", 3, 6))