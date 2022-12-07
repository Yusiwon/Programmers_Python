from itertools import combinations


def solution(number):

    number_combi = [sum(combi) for combi in list(combinations(number, 3)) if sum(combi) == 0]
    return len(number_combi)


print(solution([-1, 1, 0, 0]))
