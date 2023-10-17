from collections import defaultdict
from math import inf
def solution(n, s, a, b, fares):
    answer = []
    adj_nodes = defaultdict(list)
    for n1,n2,fare in fares: 
        adj_nodes[n1].append((n2,fare))
        adj_nodes[n2].append((n1,fare))

    def min_dist(start_node):
        dist = [inf]*(n+1)
        dist[start_node] = 0
        l = [start_node]
        while len(l) > 0:
            cur_node = l.pop(0)
            for next_node, weight in adj_nodes[cur_node]:
                if dist[next_node] > dist[cur_node] + weight:
                    dist[next_node] = dist[cur_node] + weight
                    l.append(next_node)
        return dist

    a_dist = min_dist(a)
    b_dist = min_dist(b)
    s_dist = min_dist(s)

    for i in range(1,n+1):
        answer.append(a_dist[i]+b_dist[i]+s_dist[i])
    return min(answer)

print(solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))