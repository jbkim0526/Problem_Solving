from collections import deque
n =100
si,sj= 0,0
visited = [[False for i in range(n)] for j in range(n)]

q = deque([(si,sj)])
visited[si][sj] = True

while q:
    ci,cj = q.popleft()

    # 현재 좌표의 주위 좌표들을 조사
    for di,dj in directions:
        ni,nj = i+di,j+dj

        # 범위 밖이거나 이미 조사한 좌표 이면 무시
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1 or visited[ni][nj]:
            continue

        # 갈 수 있는 좌표들이라면
        # Do something
        # 추가
        q.append((ni,nj))
        visited[ni][nj] = True