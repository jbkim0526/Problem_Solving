def solution(n, k):
    answer = []
    l = [i+1 for i in range(n)]
    factorials = [1]
    for i in range(n-1): factorials.append(factorials[i]*(i+1))
    index = n-1 ; k -= 1
    while index >= 0:
        f = factorials[index]
        q, r = k // f , k % f 
        answer.append(l[q]) ; del l[q] ; k = r ; index -= 1
    return answer

print(solution(20,2432902008176640000))