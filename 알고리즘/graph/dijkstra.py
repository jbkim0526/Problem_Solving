# 백준 1753

from collections import defaultdict
from heapq import heappop, heappush
from math import inf 

v, e = map(int,input().split())
k = int(input())
adjacents = defaultdict(set)

for _ in range(e):
    a,b,w =  map(int,input().split())
    adjacents[a].add((w,b))
    
dist = [inf]*(v+1)
heap = []
heappush(heap, (0,k))
dist[k] = 0

while heap:
    cur_dist,cur_node = heappop(heap)
    if dist[cur_node] < cur_dist:
        continue
    for w, adj_node in adjacents[cur_node]:
        new_dist = cur_dist + w
        if new_dist < dist[adj_node]:
            dist[adj_node] = new_dist
            heappush(heap,(new_dist,adj_node))

for i in range(1,v+1):
    print(dist[i] if dist[i] != inf else "INF")
