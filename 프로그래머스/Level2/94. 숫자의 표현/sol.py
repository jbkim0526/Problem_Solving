def solution(n):
    answer = 0
    l = []
    i = 0
    while True:
        v = i*(i+1)//2
        if v < n: l.append(v) ; i+=1
        else: break
    for i in range(len(l)):
        if (n - l[i]) % (i+1) == 0:
            answer +=1
    return answer

print(solution(15))