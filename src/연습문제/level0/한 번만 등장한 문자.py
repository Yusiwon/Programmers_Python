def solution(s):
    answer = []

    dic = {}

    for alpha in s:
        if alpha not in dic:
            dic[alpha] = 1
        else :
            dic[alpha] += 1

    for key, value in dic.items():
        if value == 1:
            answer.append(key)

    answer = sorted(answer)

    return ''.join(answer)

print(solution("abcabcadc"))