def solution(numbers, direction):

    if direction == 'left':
        first = numbers.pop(0)
        numbers.append(first)
    elif direction == 'right':
        end = numbers.pop()
        numbers.insert(0, end)
    return numbers


print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
