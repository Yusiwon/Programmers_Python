def solution(k, score):
    rank = []
    result = []

    for s in score:
        rank.append(s)
        rank.sort(reverse=True)

        if len(rank) > k:
            rank.pop()

        result.append(rank[len(rank)-1])

    return result

# solution(3, [10, 100, 20, 150, 1, 100, 200])
solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])