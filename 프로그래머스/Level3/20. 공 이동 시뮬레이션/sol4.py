def solution(n, m, x, y, queries):
    answer = -1
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    x_range = [x,x]
    y_range = [y,y]
    len_queries = len(queries)

    def update_range(d, r, end):
        left, right = r 
        if d < 0:
            left = left-d if left != 0 else left
            if left >= end:
                return None
            right = min(right-d,end-1)
        else:
            right = right-d if right != end-1 else right
            if right < 0:
                return None
            left = max(0,left-d)
        return [left,right]

    for i in range(len_queries-1,-1,-1):
        d, magnitude = queries[i]
        dx = directions[d][0] * magnitude
        dy = directions[d][1] * magnitude
        if dx:
            x_range = update_range(dx,x_range,n)
            if not x_range:
                return 0
        else:
            y_range = update_range(dy,y_range,m)
            if not y_range:
                return 0
        
    return (x_range[1]-x_range[0]+1)*(y_range[1]-y_range[0]+1)

print(solution(	1000, 1000, 1, 1,  [[0,100001],[2,100001]]))