def solution(k, tangerine):

    t_dic = {}

    for t in tangerine:
        if t in t_dic:
            t_dic[t] += 1
        else :
            t_dic[t] = 1

    # 딕셔너리 value기준으로 정렬
    sort_value = sorted(t_dic.items(), key=lambda x: x[1], reverse=True)

    count = 0
    for i in range(len(sort_value)):
        k -= sort_value[i][1]
        count += 1

        if k <= 0:
            break
    return count


print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
