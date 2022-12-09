def solution(num_list, n):
    answer = []

    for i in range(len(num_list) // n):
        answer.append(num_list[i * n:(i + 1) * n])
    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
