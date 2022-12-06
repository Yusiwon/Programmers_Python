def solution(string):
    right, wrong = [], []
    first = string[0]

    count = 0

    for i, s in enumerate(string):
        if s == first:
            right.append(s)
        else :
            wrong.append(s)

        if len(right) == len(wrong):
            count += 1
            if i+1 != len(string):
                first = string[i+1]

    if len(right) != len(wrong):
        count += 1
    return count

solution("banana")
solution("abracadabra")
solution("aaabbaccccabba")
