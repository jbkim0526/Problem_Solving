import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, Q = map(int,input().split())
adj_nodes = defaultdict(list)

for _ in range(N-1):
    a,b,w = map(int,input().split())
    adj_nodes[a].append((b,w))
    adj_nodes[b].append((a,w))

questions = [tuple(map(int,input().split())) for _ in range(Q)]

for k, start_node in questions:

    # BFS하면서 하나씩 조사
    visited =[0]*(N+1)
    visited[start_node] = 1
    q = deque([start_node])
    answer = 0

    while q:
        cur_node = q.popleft()
        for adj_node,w in adj_nodes[cur_node]:
            if visited[adj_node]:
                continue
            visited[adj_node] = 1
            # k 이상이 것만 추가 가능
            if w >= k:
                q.append(adj_node)
                answer += 1

    print(answer)
    