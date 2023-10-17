def prime(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(n**(1/2))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res


def solution(begin, end):
    answer = []
    primes = prime(int(end**(1/2)))
    print(primes)
    for num in range(begin,end+1):
        if num == 1 : answer.append(0) ; continue
        for p in primes:
            if num % p == 0 and  num//p <= 10000000:
                answer.append(num//p)
                break
        else:
            answer.append(1)

    return answer

#print(solution(10**8+15, 10**8+16))
print(solution(100000014, 100000016))