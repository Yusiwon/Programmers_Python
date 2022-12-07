def solution(emergency):
    answer = []
    sort_em = sorted(emergency, reverse=True)

    for e in emergency:
        index = sort_em.index(e)
        answer.append(index+1)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7]))