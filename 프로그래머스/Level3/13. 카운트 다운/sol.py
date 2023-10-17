
def solution(target):

    dp = [(0,0)]
    d = {}
    points = set([i*j for j in range(1,4) for i in range(1,21)])
    points.add(50)
    points = list(points)

    for point in points:
        d[point] = (1,0) if 1 <= point <= 20 or point == 50 else (0,1)

    for i in range(1,target+1):
        l = []
        for point in points:
            if i - point >= 0:
                a1,b1 = dp[i-point][0],dp[i-point][1]
                a2,b2 = d[point][0], d[point][1]
                l.append((a1+a2,b1+b2))
        l.sort(key= lambda x: (-(x[0]+x[1]),x[0]))
        dp.append(l[-1])
    a,b = dp[-1][0], dp[-1][1]
    return [a+b,a]

print(solution(100000))