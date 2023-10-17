def solution(n, wires):
    answer = n
    l = [[i+1] for i in range(n)]
    d = {}

    for a,b in wires:
        l[a-1].append(b)
        l[b-1].append(a)

    l.sort(key = lambda x: len(x))

    while len(l)> 0:
        isValid = True
        elem = l.pop(0)
        m = len(elem)
        target_vertex = elem[0]

        for i in range(1,m):
            adj_vertex = elem[i]
            if (target_vertex,adj_vertex) in d:
                continue
            ans = 1
            for j in range(1, m):
                if i == j:
                    continue
                other_vertex = elem[j]
                t = (other_vertex, target_vertex)
                if t in d :
                    ans += d[t]
                else:
                    l.append(elem)
                    isValid = False
                    break
            if not isValid : break
            d[(target_vertex,adj_vertex)] = ans 
            d[(adj_vertex,target_vertex)] = n - ans
            res = abs(n-2*ans)
            if res < answer:
                answer = res         

    return answer





print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))