def solution(id_list, report, k):
    answer = []
    dic = {}
    count = {}

    # 유저목록 순서대로 출력해주기때문에 딕셔너리에 순서대로 우선 형태를 잡아줌
    for user in id_list:
        dic[user] = []
        count[user] = 0

    # 신고기록 딕셔너리에 정리
    for r in report:
        user, bad = r.split(" ")

        # 같은 id 중복신고 제거
        if bad not in dic[user]:
            dic[user].append(bad)
            count[bad] += 1

    # 정지된 유저를 신고한 사람에게 확인 메일보내기 위함
    # k번 이상인지 여부를 확인/count
    for key in dic.keys():
        right = 0

        for v in dic[key]:
            if count[v] >= k:
                right += 1
        answer.append(right)
    return answer


print(
    solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],
             3))
