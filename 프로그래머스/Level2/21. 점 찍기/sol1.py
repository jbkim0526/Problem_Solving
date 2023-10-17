from math import sqrt, floor


def solution(k, d):
    answer = 1

    if k > d :
        return answer
    elif k == d : 
        answer = 3
        return answer

    # k < d :
    a = d // k
    x_bar = d /(sqrt(2))
    for i in range(1,a+1):
        x = i*k 
        if x < x_bar:
            answer += 2*i + 1
        else:
            y = floor(sqrt(d*d - x*x)) // k + 1
            answer += 2*y
    return answer


print(solution(2,5))

"""
n = 1000
for i in range(1,n):
    for j in range(1,n):
        if solution(i, j) != solution2(i,j):
            print(i,j)
            break
"""