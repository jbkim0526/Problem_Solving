
N, C = map(int,input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

l,r = 0, houses[-1]-houses[0]+1

while l+1 < r:
    mid = (l+r)//2
    current = houses[0]
    count = 1
    for i in range(1,N):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]
    if count >= C:
        l = mid 
    else:
        r = mid
    
print(l)




