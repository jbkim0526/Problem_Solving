def getCount2(n):
    res = 0
    sqrtn = int(n**(1/2))
    for i in range(1,sqrtn + 1):
        if n % i == 0:
            res += 2
    if sqrtn**2 == n:
        res -= 1
    return res

def getCount(n):
    count = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            exponent = 0
            while n % i == 0:
                n //= i
                exponent += 1
            count *= (exponent + 1)
        i += 1
    if n > 1:
        count *= 2
    return count

def solution(e, starts):
    answer = []
    d = {}
    for s in starts:
        max_count = 0
        max_num = s
        for i in range(s,e+1):
            count = 0
            if i in d: 
                count = d[i]
            else:
                count = getCount(i)
                d[i] = count
            if max_count < count:
                max_num = i 
                max_count = count
        answer.append(max_num)
    return answer

#print(solution(8,[1,3,7]))