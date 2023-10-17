
arrays = [[1,2,3],[4,5,6,7,8],["A","B","C"]]
n = len(arrays)

def track(depth,res):
    if depth == n:
        print(res)
        return
    for num in arrays[depth]:
        res.append(num)
        track(depth+1,res)
        res.pop()

track(0,[])
