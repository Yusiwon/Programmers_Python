def solution(s):
    answer = []
    dic = {}

    for index, word in enumerate(s):
        if word not in dic:
            answer.append(-1)
            dic[word] = index
        else:
            answer.append(index - dic[word])
            dic[word] = index
    return answer


print(solution("banana"))
