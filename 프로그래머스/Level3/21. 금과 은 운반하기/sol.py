from heapq import heappop,heappush,heapify

def solution(a, b, g, s, w, t):
    len_cities = len(g)
    city_time = [0]*len_cities
    city_used = [False]*len_cities
    heap = []

    for i in range(len_cities):
        heap.append(((g[i]+s[i])*t[i]/w[i],i))
    
    while a>0 or b>0:
        city = heappop(heap)[1]
        if g[city] == 0 and s[city] == 0:
            continue 
        if a == 0 and s[city] == 0:
            continue 
        if b == 0 and g[city] == 0:
            continue 

        city_weight = w[city]
        deliver_time = t[city]

        deliver_g = min(a,g[city],city_weight)
        city_weight -= deliver_g
        deliver_s = min(b,s[city],city_weight)

        g[city] -= deliver_g
        s[city] -= deliver_s
        a -= deliver_g
        b -= deliver_s

        if city_used[city]:
            city_time[city] += deliver_time 
        else:
            city_time[city] += deliver_time 
            city_used[city] = True
            t[city] *= 2
        heappush(heap,(((g[city]+s[city])*t[city]/w[city]), city))

    return max(city_time)

print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))