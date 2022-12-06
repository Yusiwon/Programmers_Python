def solution(denum1, num1, denum2, num2):
    answer = [0, 0]
    answer[0] = denum1*num2 + denum2*num1
    answer[1] = num1 * num2

    div = 1
    for i in range(2, max(answer[0], answer[1])+1):
        if answer[0]%i == 0 and answer[1]%i == 0:
            div = i

    answer[0] /= div
    answer[1] /= div

    answer[0], answer[1] = int(answer[0]), int(answer[1])
    return answer

solution(1, 2, 3, 4)