def solution(n, cores):
    l,r = 0,int(1e9)

    while l+1 < r:
        mid = (l+r)//2 
        count = 0
        for core in cores:
            count += mid//core + 1
        if count >= n:
            r = mid 
        else:
            l = mid 

    for core in cores:
        n -= (r-1)//core + 1 
    
    for i,core in enumerate(cores):
        if r % core != 0:
            continue 
        if n == 1:
            return i+1
        n -= 1
            

print(solution(	6, [1, 2, 3]))