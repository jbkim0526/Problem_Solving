from itertools import permutations

def isPrime(x):
    if x <= 1:
        return False 
    for i in range(2,int(x**(1/2))+1):
        if x % i == 0:
            return False    
    return True

def solution(numbers):
    answer = 0
    n = len(numbers)
    s = set()
    for i in range(1,n+1):
        for elem in permutations(numbers, i):
            num = 0 ; len_num = len(elem)
            for j in range(len_num):
                num += int(elem[j])*(10**(len_num-1-j))
            s.add(num)
    for elem in s:
        if isPrime(elem): 
            answer += 1
    return answer

print(solution("011"))

