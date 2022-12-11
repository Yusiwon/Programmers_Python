def solution(s):
    answer = True
    box = []
    for string in s:
        if string == ')' and len(box) == 0:
            answer = False
            break

        if string == '(':
            box.append('(')
        else :
            last = box.pop()
            if last != '(':
                answer = False
                break

    if len(box) > 0:
        answer = False
    return answer


print(solution("(()("))