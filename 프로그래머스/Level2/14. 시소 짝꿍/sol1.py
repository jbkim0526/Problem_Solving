def getBalance(w1): # returns w2 (w2 > w1) 
    ans = [2*w1]
    if 3*w1 % 2 == 0:
        ans.append(w1*3 // 2)
    if 4*w1 % 3 == 0:
        ans.append(w1*4 // 3)
    return ans


def solution(weights):
    answer = 0
    l = [0]*1001
    for w in weights:
        l[w] += 1
    for i in range(100,1001):
        if l[i] == 0:
            continue 
        n = l[i]
        answer += (n*(n-1))//2 
        balances = getBalance(i)
        for b in balances:
            if b > 1000:
                continue
            answer += l[b]*n
    return answer

print(solution([100,180,360,100,270]))