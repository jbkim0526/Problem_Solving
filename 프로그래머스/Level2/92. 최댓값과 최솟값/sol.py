def solution(s):
    l = []
    for elem in s.split():
        if elem[0] == "-": l.append(-int(elem[1:]))
        else: l.append(int(elem))
    l.sort()
    return str(l[0])+" "+str(l[-1]) 

print(solution("-1 -2 -3 -4"))