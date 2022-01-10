# 장르별 가장 많이 재생된 노래 2개씩!!
# 가장많이 재생된 장르 -> 장르내 많이 재생된 노래 -> 고유 번호 낮은 순
# 장르별 재생수를 더해서 가장 많은 거 먼저 => 같은 장르에서는 많이 재생된 거 먼저 => 각 2개 limit

def solution(genres, plays):
    answer = []
    
    # { 장르 : 총 재생 횟수 } 많은 순서 내림차순 정렬
    melon = list(zip(genres, plays))
    # melon = [('classic', 500), ('pop', 600), ('classic', 150), ('classic', 800), ('pop', 2500)]
    count = {}
    for i in melon:
        try: count[i[0]] += i[1]
        except: count[i[0]] = i[1]
   # count = {'classic': 1450, 'pop': 3100}
    sorted_count = sorted(count.items(), key = lambda item: item[1], reverse = True)
    # sorted_count = [('pop', 3100), ('classic', 1450)]
    
    
    # {장르 : [(플레이 횟수, 고유번호)]}
    playlist = {}
    for i in range(len(genres)):
        playlist[genres[i]] = playlist.get(genres[i], []) + [ (plays[i], i) ]
    # playlist= {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    for (genre, totalplay) in sorted_count:
        playlist[genre] = sorted(playlist[genre], key=lambda x: (-x[0], x[1]))
        #	[(2500, 4), (600, 1)]
        #   [(800, 3), (500, 0), (150, 2)]
    
        answer += [ idx for (play, idx) in playlist[genre][:2] ]   
    return answer