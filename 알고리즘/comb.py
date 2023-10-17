d = [1,2,3,4,5]
n = len(d)
m = 3

# combination without replacement
def track(start,res):
    if len(res) == m:
        print(res)
        return
    for i in range(start, n):
        res.append(d[i])
        track(i+1,res)
        res.pop()

#combination with replacement
def track(res):
    if len(res) == m:
        print(res)
        return
    for i in range(n):
        res.append(d[i])
        track(res)
        res.pop()

track(0,[])
