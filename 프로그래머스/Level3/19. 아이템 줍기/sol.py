# 무한루프, 실패 반례 찾으면 끝

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 50
    grid = [[0 for _ in range(N+1)] for _ in range(N+1)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    inter_coords = []
    vertex_coords = []

    for x1,y1,x2,y2 in rectangle:
        for x in range(x1,x2+1):
            if grid[x][y1] == 1: inter_coords.append((x,y1))
            else: grid[x][y1] = 1
            if grid[x][y2] == 1: inter_coords.append((x,y2))
            else: grid[x][y2] = 1

        for y in range(y1+1,y2):
            if grid[x1][y] == 1: inter_coords.append((x1,y))
            else: grid[x1][y] = 1
            if grid[x2][y] == 1: inter_coords.append((x2,y))
            else: grid[x2][y] = 1
        vertex_coords += [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]

    start_x, start_y = -1,-1
    for x in range(N+1):
        for y in range(N+1):
            if not grid[x][y]:
                continue 
            start_x, start_y = x,y
            break
        if start_x != -1: break
    cur_x, cur_y = start_x, start_y
    cur_dir = 3
    count = 0 ; character_count = 0 ; item_count = 0 

    while True:
        if (cur_x,cur_y) in inter_coords:
            cur_dir = (cur_dir - 1) % 4
        elif (cur_x,cur_y) in vertex_coords:
            cur_dir = (cur_dir + 1) % 4
        dx,dy = directions[cur_dir]
        nx, ny = cur_x+dx, cur_y+dy
        count += 1
        if nx == start_x and ny == start_y:
            break 
        if nx == itemX and ny == itemY:
            item_count = count 
        if nx == characterX and ny == characterY:
            character_count = count
        cur_x, cur_y = nx, ny

    diff = abs(character_count-item_count)
    return min(diff, abs(count-diff))

#print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1,1,2,6], [3,1,4,6], [0,2,5,3], [0,4,5,5]],2,2,4,4))