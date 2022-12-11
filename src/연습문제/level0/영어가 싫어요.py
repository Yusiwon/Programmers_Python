def solution(numbers):
    answer = 0

    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for alpha in num.keys():
        numbers = numbers.replace(alpha, num[alpha])
    return int(numbers)


print(solution("onetwothreefourfivesixseveneightnine"))

