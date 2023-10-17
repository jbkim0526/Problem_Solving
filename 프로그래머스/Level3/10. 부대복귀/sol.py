from collections import defaultdict, deque
from math import inf
def solution(n, roads, sources, destination):
    answer = []

    adj_dict = defaultdict(list)
    for r in roads:
        a,b = r[0], r[1]
        adj_dict[a].append(b)
        adj_dict[b].append(a) 
    
    dist = [inf]*(n+1)
    queue = deque() ; queue.append(destination)
    dist[destination] = 0
    while len(queue) > 0:
        cur_node = queue.popleft()
        adj_nodes = adj_dict[cur_node]
        for adj_node in adj_nodes:
            if dist[cur_node] + 1 < dist[adj_node]:
                dist[adj_node] = dist[cur_node] + 1
                queue.append(adj_node)
    
    for source in sources:
        if dist[source] == inf: answer.append(-1)
        else: answer.append(dist[source])
    return answer

print(solution(5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1, 3, 5],5))