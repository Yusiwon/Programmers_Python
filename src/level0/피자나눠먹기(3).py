def solution(slice, n):

    pizza = slice
    while n > pizza:
        pizza += slice
    return pizza//slice


# solution(7, 10)
solution(4, 12)