def solution(n):
    answer = []

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer.append(i)
            if i*i != n:
                answer.append(n//i)

    answer = sorted(answer)
    return answer


print(solution(29))