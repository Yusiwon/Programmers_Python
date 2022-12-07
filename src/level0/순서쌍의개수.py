def solution(n):
    answer = 0

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                answer += 1   # 5*5와 같이 같은수의 곱셈인 경우
            else :
                answer += 2
    return answer

print(solution(100))