from collections import Counter


def solution(X, Y):
    answer = ''

    x = Counter(X)
    y = Counter(Y)
    inter = x.keys() & y.keys()

    if len(inter) == 0:
        return "-1"
    else:
        num = []
        for i in inter:
            for j in range(min(x[i], y[i])):
                num.append(i)

        num = sorted(num, reverse=True)

    # return => after list to string
    if num.count('0') == len(num):
        return "0"
    return ''.join(num)


print(solution("100", "203045"))
