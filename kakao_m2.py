def solution(id_list, k):
    cnt = dict()
    for daily_id_list in id_list:
        daily_ids = set(daily_id_list.split())
        for id in daily_ids:
            if cnt.get(id) == None:
                cnt[id] = 1
            elif cnt[id] < k:
                cnt[id] += 1
    ans = sum(cnt.values())
    return ans

print(solution(
["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))