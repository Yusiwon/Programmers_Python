def solution(rsp):
    answer = ''

    win = {'2' : "0", "0" : "5", "5" : "2"}

    for l in rsp:
        answer += win[l]
    return answer

print(solution("205"))