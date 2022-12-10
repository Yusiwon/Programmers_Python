def solution(s):
    answer = 0
    num = []

    for string in s.split(" "):
        if string == 'Z':
            num.pop()
        else:
            num.append(int(string))

    return sum(num)


print(solution("10 20 30 40"))
