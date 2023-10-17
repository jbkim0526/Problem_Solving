import sys 
input = sys.stdin.readline 

n, m = map(int, input().split())

dleft = []

for _ in range(n):
    a,b = map(int,input().split())
    if a > b : dleft.append((b,a))

dleft.sort()

def getUnion(d):
    res = []
    start = d[0][0]
    end = d[0][1]
    for a,b in d:
        if a<= end:
            end = max(end,b)
            continue 
        res.append((start,end))
        start = a
        end = b 
    res.append((start,end))
    return res

left_res = getUnion(dleft)
ans = 0
cur_num = 0

for a,b in left_res:
    ans += 2*b - cur_num - a
    cur_num = a
ans += m-cur_num

print(ans)




