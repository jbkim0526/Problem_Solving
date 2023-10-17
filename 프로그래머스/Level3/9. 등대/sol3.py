import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def solution(n, lighthouse):

    dp = [[0,0] for _ in range(n+1)]
    adj_d = defaultdict(set)
    visited = [False]*(n+1)
    for node in lighthouse:
        a,b = node[0], node[1]
        adj_d[a].add(b) ; adj_d[b].add(a)
    
    def track(node):
        visited[node] = True
        adj_nodes = adj_d[node]
        next_nodes = []
        for adj_node in adj_nodes:
            if visited[adj_node]:
                continue
            next_nodes.append(adj_node)
            track(adj_node)
        dp[node][0] = 0 ; dp[node][1] = 1
        for next_node in next_nodes:
            dp[node][1] += min(dp[next_node])
            dp[node][0] += dp[next_node][1]
    track(1)
    return min(dp[1])

print(solution(10,[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
        




