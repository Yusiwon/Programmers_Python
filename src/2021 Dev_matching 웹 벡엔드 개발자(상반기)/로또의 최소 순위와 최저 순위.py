def solution(lottos, win_nums):
    lotto = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    correct = 0
    zero = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            correct += 1
        print(f'num = {num} \n correct = {correct} zero = {zero}')

    return [lotto[correct+zero], lotto[correct]]

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))