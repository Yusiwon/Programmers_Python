def solution(sizes):
    answer = 0

    for size in sizes:
        # [0] > [1] 형태로 만들어주기 위함
        if size[0] < size[1]:
            temp = size[1]
            size[1] = size[0]
            size[0] = temp

    # [0]과 [1]에서 가장 큰값을 구하기
    width = max([x[0] for x in sizes])
    height = max([x[1] for x in sizes])
    return width*height


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))