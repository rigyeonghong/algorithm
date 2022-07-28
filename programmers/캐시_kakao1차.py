def solution(cacheSize, cities):
    cnt = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    upper_cities = []
    for c in cities:
        upper_cities.append(c.upper())
    cache = [upper_cities[0]]
    
    for i in range(1, len(upper_cities)):
        if len(cache) < cacheSize:
            if upper_cities[i] in cache:
                cnt += 1
                idx = cache.index(upper_cities[i])
                cache.pop(idx)
                cache.append(upper_cities[i])
            else:
                cache.append(upper_cities[i])
                cnt += 5
        else:
            if upper_cities[i] in cache:
                cnt += 1
                idx = cache.index(upper_cities[i])
                cache.pop(idx)
                cache.append(upper_cities[i])
            else:
                cache.pop(0)
                cache.append(upper_cities[i])
                cnt += 5   
    return cnt + 5

# modify
def solution(cacheSize, cities):
    time = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    upper_cities = []
    for c in cities:
        upper_cities.append(c.upper())
    cache = [upper_cities[0]]
    
    for i in range(1, len(upper_cities)):
        if len(cache) < cacheSize:
            if upper_cities[i] in cache:
                time += 1
                cache.remove(upper_cities[i])
                cache.append(upper_cities[i])
            else:
                cache.append(upper_cities[i])
                time += 5
        else:
            if upper_cities[i] in cache:
                time += 1
                cache.remove(upper_cities[i])
                cache.append(upper_cities[i])
            else:
                cache.pop(0)
                cache.append(upper_cities[i])
                time += 5   
    return time + 5

# reference
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time