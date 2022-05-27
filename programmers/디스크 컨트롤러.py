import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            # 시점을 체크함  바로 이전에 완료한 작업 시작 시간 < 시점 <= 현재 시점
            if start < j[0] <= now:
                #  작업 소요시간 기준으로 최소힙 만들어야함 : [작업의 소요 시간, 작업이 요청되는 시점]
                heapq.heappush(heap, [j[1], j[0]])
                
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
            
        else:
            now += 1
    return int(answer / len(jobs))