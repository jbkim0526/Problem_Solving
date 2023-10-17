from collections import defaultdict
from math import inf
def solution(n, edge):
    adj_nodes = defaultdict(set)
    for a,b in edge:
        adj_nodes[a].add(b)
        adj_nodes[b].add(a)

    score = [inf]*(n+1)
    score[1] = 0
    l = [1]

    while len(l) > 0:
        cur_node = l.pop(0)
        for adj_node in adj_nodes[cur_node]:
            next_score = score[cur_node] + 1
            if score[adj_node] > next_score:
                score[adj_node] = next_score
                l.append(adj_node)

    max_dist = max(score[1:])
    return score.count(max_dist)





print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))