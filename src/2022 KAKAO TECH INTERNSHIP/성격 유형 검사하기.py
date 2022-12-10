def solution(survey, choices):
    answer = ''

    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for s, c in zip(survey, choices):
        if c < 4:
            dic[s[0]] += 4 - c
        elif c > 4:
            dic[s[1]] += c - 4

    kakao = list(dic.keys())
    for i in range(0, 8, 2):
        left = dic[kakao[i]]
        right = dic[kakao[i+1]]

        if left >= right:
            answer += kakao[i]
        else :
            answer += kakao[i+1]
    return answer


print(solution(["TR", "RT", "TR"], [7, 1, 3]))
