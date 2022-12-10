def solution(my_string):
    answer = ''

    string = []
    for s in my_string:
        if s not in string:
            string.append(s)
    return ''.join(string)


print(solution("We are the world"))
