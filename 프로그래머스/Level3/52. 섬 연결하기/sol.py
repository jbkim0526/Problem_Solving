from collections import defaultdict
from heapq import heapify, heappop, heappush

def solution(n, costs):
    answer = 0
    next_nodes = defaultdict(set)

    for a,b,cost in costs:
        next_nodes[a].add((cost,b))
        next_nodes[b].add((cost,a))

    visited = [False]*n
    heap = []
    heappush(heap, (0,0))

    while len(heap) > 0:
        cost,cur_node = heappop(heap)
        if visited[cur_node]:
            continue 
        visited[cur_node] = True 
        answer += cost 

        for next_cost, next_node in next_nodes[cur_node]:
            if visited[next_node]:
                continue 
            heappush(heap,(next_cost,next_node))
    return answer

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))