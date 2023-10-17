from math import ceil, floor, sqrt 

def solution(r1, r2):
    answer = 0
    
    
    for i in range(1,r1+1):
        a = ceil(sqrt(r1*r1 - i*i))
        b = floor(sqrt(r2*r2 - i*i))
        answer = answer + b-a +1 
    for i in range(r1+1,r2+1):
        a = 0
        b = floor(sqrt(r2*r2 - i*i))
        answer = answer + b-a +1
        
    return answer*4

print(solution(2,3))