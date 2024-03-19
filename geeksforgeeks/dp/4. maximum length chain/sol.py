def maxChainLen(self,p,n):

    p.sort(key=lambda x: x.b)
    prev = -1e9
    ans = 0
    for x in p:
        if x.a > prev:
            ans += 1
            prev = x.b
    return ans