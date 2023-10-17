from collections import defaultdict
from heapq import heappush,heappop,heapify
from math import inf

def solution(k, n, reqs):
    answer = 0

    participants = defaultdict(list)
    waiting_times = [[] for _ in range(k+1)]

    for stime,duration,t in reqs:
        participants[t].append((stime,duration))

    for t,times in participants.items():
        for mentor_num in range(1,len(times)+1):
            heap = []
            waiting_time = 0
            for i in range(len(times)):
                stime, dtime = times[i]
                if len(heap) < mentor_num:
                    heappush(heap, stime+dtime)
                    continue 
                endtime = heappop(heap)
                if endtime > stime:
                    waiting_time += endtime-stime
                    heappush(heap, endtime+dtime)
                else:
                    heappush(heap, stime+dtime)
            waiting_times[t].append(waiting_time)
    
    def track(t,n):
        if n == 0 or t > k:
            return 0
        ans = []
        waiting_time = waiting_times[t]
        if len(waiting_time) == 0:
            return track(t+1,n-1)
        m = min(n,len(waiting_time))
        for i in range(m):
            if n < i+1 or (t == k and n != i+1) or (t != k and n == i+1):
                continue
            ans.append(waiting_time[i]+track(t+1,n-(i+1)))
        if len(ans) == 0:
            return inf
        return min(ans)

    return track(1,n)



#print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))
print(solution(2,3,[[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))