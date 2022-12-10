def solution(elements):
    # 기본 리스트의 중복제거를 위해 set을 이용함
    result = set(elements)
    double_element = elements * 2

    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            result.add(sum(double_element[j:j + i]))

    return len(result)


print(solution([7, 9, 1, 1, 4]))
