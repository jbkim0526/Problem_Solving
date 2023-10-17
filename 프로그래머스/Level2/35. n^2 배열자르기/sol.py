def solution(n, left, right):
    answer = []
    lg, rg = left//n + 1 , right//n + 1
    li, ri = left % n, right % n
    if lg == rg :
        answer += ([lg]*lg + [i for i in range(lg+1,n+1)])[li:ri+1]
    else:
        answer += ([lg]*lg + [i for i in range(lg+1,n+1)])[li:]
        for i in range(lg+1,rg):
            answer += [i]*i + [j for j in range(i+1,n+1)]
        answer += ([rg]*rg + [i for i in range(rg+1,n+1)])[:ri+1]
    return answer


print(solution(4,0,3))