def solution(ingredient):
    answer = 0
    store = []
    for burger in ingredient:
        store.append(burger)

        if store[-4:] == [1, 2, 3, 1]:
            answer += 1

            store.pop()
            store.pop()
            store.pop()
            store.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))