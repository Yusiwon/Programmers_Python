def solution(babbling):
    answer = 0

    for word in babbling:
        index = 0

        for i in range(1, len(word)+1):
            if word[index:i] in ['aya', 'ye', 'woo', 'ma']:
                index = i

        if index == len(word):
            answer += 1
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))