def solution(n):
    answer = 0

    if n in [1, 2, 3]:
        return 0
    else :
        for i in range(4, n+1):
            count = 0
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    count += 1
                    if j*j != i:
                        count += 1

            if count >= 3:
                answer += 1

    return answer


print(solution(15))