from collections import defaultdict

def solution(beginning, target):
    h,w = len(target),len(target[0])
    grid = [[1 if beginning[i][j] == target[i][j] else 0 for j in range(w)] for i in range(h)]
    col_dict = defaultdict(int)
    row_dict = defaultdict(int)
    for row in grid:
        row_dict[tuple(row)] += 1
    for j in range(w):
        t = []
        for i in range(h):
            t.append(grid[i][j])
        col_dict[tuple(t)] += 1
    if len(row_dict) > 2 or len(col_dict) > 2:
        return -1
    else:
        rows = list(row_dict.keys())
        cols = list(col_dict.keys())

        if len(rows) == 1:
            return rows[0].count(0)
        elif len(rows) == 2:
            r1,r2 = rows[0], rows[1]
            for i in range(w): 
                if not r1[i] ^ r2[i]: return -1 
            return min(row_dict[r1]+r1.count(1), row_dict[r2]+r2.count(1))
                    

         

#print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
#print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))