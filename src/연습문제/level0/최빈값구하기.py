def solution(array):
    answer = {}

    for a in array:
        if a not in answer:
            answer[a] = 1
        else:
            answer[a] += 1

    high = max(answer.values())

    result = []
    for key in answer.keys():
        if answer[key] == high:
            result.append(key)

    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        return -1

# solution([1, 2, 3, 3, 3, 4])
# solution([1, 1, 2, 2])
solution([1])