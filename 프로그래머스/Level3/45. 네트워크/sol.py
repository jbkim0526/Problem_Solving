from collections import defaultdict

def solution(n, computers):
    answer = 0
    adj_computers = defaultdict(set)
    visited = [False]*n
    for i in range(n):
        for j in range(i):
            if not computers[i][j]:
                continue 
            adj_computers[i].add(j)
            adj_computers[j].add(i)

    for i in range(n):
        if visited[i]:
            continue 
        l = [i]
        while len(l) > 0:
            cur_com = l.pop(0)
            visited[cur_com] = True
            for adj_com in adj_computers[cur_com]:
                if visited[adj_com]:
                    continue
                l.append(adj_com)
        answer += 1
        
    return answer


print(solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))