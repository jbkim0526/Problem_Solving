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
    l = [0]*(e+1)
    for num in range(e,0,-1):
        l[num] = getCount(num)
        print(num)
    for s in starts:
        max_count = 0
        max_num = s
        for num in range(s,e+1):
            count = l[num]
            if max_count < count:
                max_num = num
                max_count = count 
        answer.append(max_num)
    return answer

print(solution(5000000,[1,3,7]))



