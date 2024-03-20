from collections import defaultdict
from heapq import heappop, heappush
v, e = map(int,input().split())

adjacents = defaultdict(set)

for _ in range(e):
    a,b,w = map(int,input().split())
    adjacents[a].add((b,w))
    adjacents[b].add((a,w))


visited = set()
mst = []
ans = 0
heap = [(0,1,1)]

while heap:
    w, pre_node, cur_node = heappop(heap)
    print(cur_node, w, visited)
    mst.append((pre_node,cur_node))
    ans += w 
    visited.add(cur_node)

    for next_node, next_w in adjacents[cur_node]:
        if next_node in visited:
            continue
        print(next_w,cur_node, next_node)
        heappush(heap,(next_w,cur_node,next_node))

print(ans)