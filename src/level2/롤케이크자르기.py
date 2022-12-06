from collections import Counter

def solution(topping):

    dic = Counter(topping)    # 딕셔너리 형태로 담긴다

    set_dic = set()
    count = 0

    for t in topping:
        dic[t] -= 1
        set_dic.add(t)

        if dic[t] == 0:
            dic.pop(t)

        if len(dic) == len(set_dic):
            count += 1

    return count

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))