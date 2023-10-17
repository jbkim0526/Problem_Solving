from math import inf
def solution(N, road, K):
    answer = 0
    l = [[inf if i != j else 0 for j in range(N)] for i in range(N)]
    for r in road:
        a,b,d = r[0]-1, r[1]-1, r[2]
        l[a][b] = min(d,l[a][b])
        l[b][a] = min(d,l[b][a])

    d = [0]+[inf]*(N-1)
    bfs = [0]
    
    while len(bfs) > 0:
        cur_i = bfs.pop(0)
        for j in range(N):
            if l[cur_i][j] != inf:
                newd = d[cur_i]+l[cur_i][j]
                if newd < d[j]:
                    d[j] = newd 
                    bfs.append(j)
               
    for i in range(N):
        if d[i] <= K:
            answer += 1 
    return answer


print(solution(6,[[1,2,5],[1,3,1],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))