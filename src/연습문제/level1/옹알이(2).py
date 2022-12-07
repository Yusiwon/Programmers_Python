def solution(babbling):
    answer = 0

    word_arr = ['aya', 'ye', 'woo', 'ma']

    for talk in babbling:

        for word in word_arr:
            if word*2 not in talk:
                talk = talk.replace(word, ' ')

        if talk.strip() == '':
            answer += 1

    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
