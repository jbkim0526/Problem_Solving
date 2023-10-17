def solution(n, cores):
    hour = 0
    res = []
    while True:
        for i,core in enumerate(cores):
            if hour % core != 0:
                continue 
            res.append(core)
            if len(res) == n:
                return i+1
        hour += 1

    
print(solution(6,	[1,2,3]))