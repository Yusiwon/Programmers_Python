############### 최종 완성 코드 ####################
def solution(number, limit, power):

    result = 1

    for n in range(2, number+1):
        div_cnt = 2   # 약수

        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                div_cnt += 1

                if (i**2) != n:    # 같은수의 제곱인 경우를 제외하는 조건
                    div_cnt += 1

        if div_cnt > limit :
            result += power
        else :
            result += div_cnt

    return result

solution(5, 3, 2)