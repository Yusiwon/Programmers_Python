def solution(s):

    words = list(s.lower())
    words[0] = words[0].upper()

    for i in range(1, len(words)-1):
        if words[i] == ' ':
            words[i+1] = words[i+1].upper()
    return ''.join(words)


print(solution("abc ddd 123abc  "))