import sys 
from heapq import heappush,heappop
from math import inf
input = sys.stdin.readline 

N = int(input())
bus = [dict() for _ in range(N+1)]
visited = [False for _ in range(N+1)]
score = [inf for _ in range(N+1)]
records = dict()

for _ in range(int(input())):
    a,b,cost = map(int,input().split())
    bus[a][b] = cost 

start,end = map(int,input().split())
score[start] = 0
heap = []
heappush(heap, (0,start,-1))

while heap:
    cur_score, cur_city, before_city = heappop(heap)
    if score[cur_city] < cur_score:
        continue
    visited[cur_city] = True
    records[cur_city] = before_city
    for next_city, bus_cost in bus[cur_city].items():
        next_score = cur_score + bus_cost
        if next_score < score[next_city]:
            score[next_city] = next_score
            heappush(heap, (next_score,next_city,cur_city))

print(score[end])

# answer = [str(end)]
# cur_city = end 
# while cur_city != start:
#     cur_city = records[cur_city]
#     answer.append(str(cur_city))
# answer.reverse()


# print(len(answer))
# print(" ".join(answer))