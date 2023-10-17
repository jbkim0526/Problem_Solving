from collections import defaultdict

def solution(n, moneys):
    answer = 0
    moneys.sort(reverse= True)
    dp = defaultdict(dict)
    len_moneys = len(moneys)
    tuple_lists,l = [None]*len_moneys,[]

    for i,money in enumerate(moneys):
        l.append(money)
        tuple_lists[-1-i] = tuple(l)


    def track(n,depths):
        if n == 0:
            return 1
        if depths >= len_moneys:
            return 0
        t = tuple_lists[depths]
        money = t[-1]
        if money > n:
            return 0
        d = dp[n]
        if depths in d:
            return d[depths] 
        ans = 0
        q = n // money 
        for i in range(q,-1,-1):
            ans += track(n- money*i,depths+1) 
        d[depths] = ans % 1000000007
        return d[depths] 

    return track(n,0)



#print(solution(5,[1,2]))
print(solution(100000, [i for i in range(1,101)]))