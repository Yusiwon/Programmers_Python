def solution(n):

    pizza = 6
    while True:
        if pizza % n == 0:
            break

        pizza += 6

    return pizza // 6


solution(10)