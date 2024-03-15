# 백준 1197번

from collections import defaultdict
from heapq import heappop, heappush
v, e = map(int,input().split())

adjacents = defaultdict(set)

for _ in range(e):
    a,b,w = map(int,input().split())
    adjacents[a].add((b,w))
    adjacents[b].add((a,w))

heap = []
visited = set()
mst = []
ans = 0
# 임의로 1번 node 선택
visited.add(1)
for adj_node,w in adjacents[1]:
    heappush(heap,(w,1,adj_node))

while len(visited) < v:
    w, pre_node, cur_node = heappop(heap)
    if cur_node in visited:
        continue
    mst.append((pre_node,cur_node))
    ans += w 
    visited.add(cur_node)

    for next_node, next_w in adjacents[cur_node]:
        if next_node in visited:
            continue
        heappush(heap,(next_w,cur_node,next_node))

print(ans)




