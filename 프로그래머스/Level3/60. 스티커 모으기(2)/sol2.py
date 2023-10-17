from heapq import heappush, heappop

def solution(sticker):
    answer = 0
    n = len(sticker)
    visited = [False for _ in range(n)]
    heap = []

    def getScore(i):
        v = 0 if visited[i] else sticker[i]
        lv = 0 if visited[(i-1)%n] else sticker[(i-1)%n]
        rv = 0 if visited[(i+1)%n] else sticker[(i+1)%n]
        return lv+rv-v
    
    for i in range(n):
        heappush(heap,(getScore(i),i))
    
    while len(heap) > 0:
        score, i = heappop(heap)
        if visited[i]:
            continue 
        answer += sticker[i]
        visited[i] = True 
        visited[(i-1)%n] = True 
        visited[(i+1)%n] = True 
        li,ri = (i-2)%n, (i+2)%n
        heappush(heap, (getScore(li),li))
        heappush(heap, (getScore(ri),ri))

    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))