def solution(price, money, count):

    # 총 내야할 놀이기구 금액
    give = 0
    for i in range(1, count + 1):
        give += price * i

    if give > money:
        return give - money
    else:
        return 0


print(solution(2, 20, 4))
