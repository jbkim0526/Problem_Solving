from collections import defaultdict
from math import inf
def solution(n, paths, gates, summits):
    answer = []
    edges = {}
    adj_nodes = defaultdict(list)

    for path in paths:
        a,b,d = tuple(path)
        edges [(a,b)] = d
        edges [(b,a)] = d
        adj_nodes[a].append(b)
        adj_nodes[b].append(a)

    s = []

    

    for gate in gates:
        intensity = [inf]*(n+1)
        intensity[gate] = 0  
        l = [gate]

        def track(l, summit):
            
            if len(l) == 0:
                return 0,summit
            cur_node = l.pop(0)
            cur_node_score = intensity[cur_node]
            for adj_node in adj_nodes[cur_node]:
                if summit and adj_node in summit:
                    continue 
                if adj_node in gates:
                    continue
                next_score = max(cur_node_score, edges[(cur_node,adj_node)])
                if intensity[adj_node] > next_score:
                    intensity[adj_node] = next_score 
                    l.append(adj_node)
                    if adj_node in summit:
                        i,s = track(l.copy(),adj_node)
                    else:
                        i,s = track(l.copy(),adj_node)
                
            


        while len(l) > 0:
            cur_node = l.pop(0)
            cur_node_score = intensity[cur_node]
            for adj_node in adj_nodes[cur_node]:
                next_score = max(cur_node_score, edges[(cur_node,adj_node)])
                if intensity[adj_node] > next_score:
                    intensity[adj_node] = next_score 
                    l.append(adj_node)

        for summit in summits:
            s.append((summit,intensity[summit]))

    s.sort(key = lambda x: (-x[1],-x[0]))
    return [s[-1][0],s[-1][1]]


print(solution(	7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))