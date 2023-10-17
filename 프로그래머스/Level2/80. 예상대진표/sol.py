def solution(n,a,b):
    answer = 1

    while True:
        
        a = a//2 + 1 if a % 2 != 0 else a//2
        b = b//2 + 1 if b % 2 != 0 else b//2
        if a == b: return answer
        answer += 1
    return answer