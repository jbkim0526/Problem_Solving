d = [1,2,3,4,5]
n = len(d)
m = 3


def comb_without_replacement(start,res):
    if len(res) == m:
        print(res)
        return 
    for i in range(start,n):
        res.append(d[i])
        comb_without_replacement(i+1, res)
        res.pop()
    return

def comb_with_replacement(res):
    if len(res) == m:
        print(res)
        return 
    for i in range(n):
        res.append(d[i])
        comb_with_replacement(res)
        res.pop()
    return

#comb_without_replacement(0,[])
#comb_with_replacement([])

def perm_without_replacement(res):
    if len(res) == m:
        print(res)
        return
    for i in range(n):
        if d[i] in res:
            continue
        res.append(d[i])
        perm_without_replacement(res)
        res.pop()

def perm_with_replacement(res):
    if len(res) == m:
        print(res)
        return
    for i in range(n):
        res.append(d[i])
        perm_with_replacement(res)
        res.pop()

#perm_without_replacement([])
perm_with_replacement([])
