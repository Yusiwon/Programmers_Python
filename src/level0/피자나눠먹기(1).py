def solution(n):

    pizza = 7
    while n > pizza:
        pizza += 7
    return pizza//7


solution(15)