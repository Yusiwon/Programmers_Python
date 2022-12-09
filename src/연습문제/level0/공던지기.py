def solution(numbers, k):
    answer = 0

    for i in range(k-1):
        if answer + 2 == len(numbers):
            answer = 0
        elif answer + 2 == len(numbers)+1:
            answer = 1
        else:
            answer += 2

    return numbers[answer]


print(solution([1, 2, 3], 3))
