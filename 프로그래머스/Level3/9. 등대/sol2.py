# greedy이고 변화된 수치까지 재정렬 해서 반영 -> time 초과 안나지만 fail

from collections import defaultdict
from bisect import bisect_left
def solution(n, lighthouse):
    answer = 0
    adj_d = defaultdict(set)
    count_d = defaultdict(list)
    l = []

    for i in range(n):
        count_d[i+1].append(0)
        count_d[i+1].append(i+1)
        l.append(count_d[i+1])

    for light in lighthouse:
        a,b = light[0], light[1]
        adj_d[a].add(b) ; adj_d[b].add(a)
        count_d[a][0] += 1 ; count_d[b][0] += 1
    
    l.sort(key= lambda x: x[0])
    while n-1 > 0:
        i = l.pop()[1]
        if i == -1:
            continue
        adj_nodes = adj_d[i]
        count_d[i][0] = 0
        for node in adj_nodes:
            temp = count_d[node].copy()
            temp[0] -= 1
            a = bisect_left(l, temp)
            l.insert(a, temp)
            count_d[node][1] = -1
            n -= 1
        answer += 1
    return answer

print(solution(9, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]))