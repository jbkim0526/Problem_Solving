from itertools import combinations

def solution(orders, course):
    answer = []
    n_order = len(orders)

    set_orders = []
    d = []
    counts = []
    for order in orders:
        set_orders.append(set(order))

    for i in range(n_order):
        si = set_orders[i]
        l = [si]
        for j in range(2,len(si)):
            for elem in list(combinations(si, j)):
                l.append(set(elem))
        for target in l:
            for j in range(i+1,n_order):
                s = target.intersection(set_orders[j])
                if len(s) >= 2 and s not in d:
                    d.append(s)

    for elem in d:
        count = 0
        for order in set_orders:
            if elem.issubset(order):
                count +=1 
        counts.append(count)

    for course in course:
        maxlen = -1
        ans = []
        for i in range(len(d)):
            if len(d[i]) == course:
                c = counts[i] 
                if c > maxlen:
                    ans = []
                    ans.append(d[i])
                    maxlen = c
                elif c == maxlen:
                    ans.append(d[i])
        for a in ans:
            a = list(a)
            a.sort()
            answer.append("".join(a))
    answer.sort()
    return answer


print(solution(["ABCFG", "ABC"]	,[2,4]))
