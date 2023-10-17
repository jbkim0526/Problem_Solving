
def solution(begin, end):
    answer = []
    for num in range(begin,end+1):
        if num == 1 : answer.append(0) ; continue
        l = []
        flag = True
        for p in range(2,int(num**(1/2))+1):
            if num % p == 0:
                if num//p <= 10000000:
                    answer.append(num//p)
                    flag = False
                    break
                else:
                    l.append(p)
        if flag:
            if len(l) == 0:
                answer.append(1)
            else:
                answer.append(max(l))
    return answer

print(solution(100000014, 100000016))