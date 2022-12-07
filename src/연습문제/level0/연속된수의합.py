def solution(num, total):
    answer = []

    mid = total // num

    return [x for x in range(mid - ((num-1)//2), mid + 1 + (num//2))]


print(solution(5, 5))
