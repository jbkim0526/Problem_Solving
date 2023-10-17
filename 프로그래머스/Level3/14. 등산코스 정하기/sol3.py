from collections import defaultdict
from heapq import heapify,heappop,heappush

def solution(n, paths, gates, summits):
    adj_nodes = defaultdict(list)
    summits.sort()
    summits_set = set(summits)
    for a,b,d in paths:
        adj_nodes[a].append((b,d))
        adj_nodes[b].append((a,d))
    inf = 10000001
    heap = []
    intensity = [inf]*(n+1)
    for gate in gates:
        heap.append((0,gate))
        intensity[gate] = 0  
    
    heapify(heap)

    while heap:
        cur_node_score, cur_node = heappop(heap)

        if cur_node in summits_set or cur_node_score > intensity[cur_node]:
            continue

        for adj_node, d in adj_nodes[cur_node]:
            next_score = max(cur_node_score, d)
           
            if intensity[adj_node] > next_score:
                intensity[adj_node] = next_score 
                heappush(heap, (next_score,adj_node))
    
    answer = [0, inf]
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer[0] = summit
            answer[1] = intensity[summit]

    return answer

print(solution(	7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))