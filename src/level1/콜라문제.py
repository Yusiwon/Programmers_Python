def solution(a, b, n):
    answer = []

    while True:
        if n < a:
            break
        remain = n%a
        n = n//a * remain
        answer.append(n*b)
        n += remain

        print(f'remain : {remain}\n answer : {answer}\n n : {n}')

    return sum(answer)


# solution(2, 1, 20)
solution(3, 1, 20)