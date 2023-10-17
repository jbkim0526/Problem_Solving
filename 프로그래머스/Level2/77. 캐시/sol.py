from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen= cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            cache.append(city)
            answer += 5
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))



