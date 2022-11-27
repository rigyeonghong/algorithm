def solution(s, times):
    # [첫 저축, 다음 저축까지 기간들 ]
    answer = [0, 0]
    # [2021, 4, 12, 16, 8, 35] 년 월 일2 시3 분4 초5
    first = list(map(int, s.split(":")))
    # 1. 1일 1 저축 성공 여부
    flag = 1
    check = first[2] # 12일
    daily = [] # [2021, 4, 12, 16, 8, 35] 년0 월1 일2 시3 분4 초5
    for item in first:
        daily.append(item)
    for time in times:
        # [1, 6, 30, 0] 일0, 시1, 분2, 초3
        term = list(map(int, time.split(":")))
        sec = (daily[5] + term[3]) % 60 # 초
        minute = (daily[4] + term[2]) % 60 + (daily[5] + term[3]) // 60
        hour = (daily[3] + term[1]) % 24 + (daily[4] + term[2]) // 60
        day = (daily[2] + term[0]) + (daily[3] + term[1]) // 24
        
        daily[5] = sec # 초
        daily[4] = minute % 60 #분
        daily[3] = ((hour % 24) + (minute // 60)) % 24 #시
        daily[2] =  day +(hour // 24) + ((hour % 24) + (minute // 60)) // 24  #일 
        print(daily)
        if daily[2] - check > 1:
            flag = 0
        else:
            check = daily[2]
    answer[0] = flag

    # 2. 저축기간(일)은 첫 저축과 마지막 일만 비교
    # first [2021, 4, 12, 16, 8, 35] 년0 월1 일2 시3 분4 초5
    # daily [2021, 4, 15, 2, 50, 35] 년0 월1 일2 시3 분4 초5
    answer[1] = daily[2] - first[2] +1
    # return [성공여부(int), 저축기간(일)]
    return answer

print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"]))