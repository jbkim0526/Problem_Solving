
def gd(n):
    if n == 1:
        return 0
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            print(n,i)
            return n // i 
    return 1



def solution(begin, end):
    answer = []
    for num in range(begin,end+1):
        answer.append(gd(num))
    return answer

print(solution(10**9-3, 10**9))