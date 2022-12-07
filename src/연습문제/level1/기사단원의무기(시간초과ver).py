############### 시간 초과 발생! ####################
def solution(number, limit, power):

    result = 1

    for n in range(2, number+1):
        div_cnt = 2   # 약수
        for i in range(2, n):
            if n % i == 0:
                div_cnt += 1

        if div_cnt > limit :
            result += power
        else :
            result += div_cnt

    return result

solution(5, 3, 2)