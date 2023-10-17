def find_figures(board, num):
    figures = []
    row_len = len(board)
    col_len = len(board[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for row in range(row_len):
        for col in range(col_len):
            if board[row][col] != num:
                continue 
            l = [(row,col)]
            b = []
            while len(l) > 0:
                cur_x,cur_y = l.pop(0)
                b.append((cur_x-row,cur_y-col))
                board[cur_x][cur_y] = 1 if num == 0 else 0
                for dx,dy in directions:
                    nx,ny = cur_x+dx, cur_y+dy
                    if 0 <= nx < row_len and 0 <= ny < col_len and board[nx][ny] == num:
                        l.append((nx,ny))
            figures.append(b)
    return figures

def make_figure_list(figures):
    l = []
    for board_figure in figures:
        min_x,max_x = 50,-1
        min_y,max_y = 50,-1
        for x,y in board_figure:
            min_x = min(min_x,x)
            max_x = max(max_x,x)
            min_y = min(min_y,y)
            max_y = max(max_y,y)
        figure = [[0 for _ in range(max_y-min_y+1)] for _ in range(max_x - min_x + 1)]
        for x,y in board_figure:
            figure[x-min_x][y-min_y] = 1
        l.append(figure)
    return l


def getRotatedList(l):
    m = len(l)
    n = len(l[0])
    res = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            res[j][i] = l[i][j]
    for row in range(n):
        res[row].reverse()
    return res

def make_figure_set(figure_list):
    l = []
    for figure in figure_list:
        figure_set = set()
        figure_set.add(tuple(map(tuple, figure)))

        rotated90_list = getRotatedList(figure)
        t90 = tuple(map(tuple, rotated90_list))
        if t90 in figure_set:
            l.append(figure_set) 
            continue 
        figure_set.add(t90)

        rotated180_list = getRotatedList(rotated90_list)
        t180 = tuple(map(tuple, rotated180_list))
        if t180  in figure_set:
            l.append(figure_set) 
            continue 
        figure_set.add(t180)

        rotated270_list = getRotatedList(rotated180_list)
        t270 = tuple(map(tuple, rotated270_list))
        if t270 in figure_set:
            l.append(figure_set) 
            continue 
        figure_set.add(t270)
        l.append(figure_set) 
    return l

def count_one(tup):
    res = 0
    for row in tup :
        for elem in row:
            res += elem 
    return res


def solution(game_board, table):
    answer = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    board_figures = find_figures(game_board, 0)
    table_figures = find_figures(table, 1)

    board_figure_list = make_figure_list(board_figures)
    table_figure_list = make_figure_list(table_figures)

    board_figure_set = make_figure_set(board_figure_list)
    table_figure_set = make_figure_set(table_figure_list)

    for i, table_figure in enumerate(table_figure_set):
        for board_figure in board_figure_set:
            if table_figure != board_figure:
                continue 
            board_figure_set.remove(board_figure)
            answer += count_one(table_figure_list[i])
            break
    return answer

print(solution(	[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))



  