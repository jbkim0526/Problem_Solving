N = int(input())
k = int(input())

l,r = 0, int(min(1e9, N*N))+1

while l+1<r:

    # mid = B[k]로 추정하는 값
    mid = (l+r)//2

    # count = mid 보다 작거나 같은 숫자의 개수
    count = 0
    for i in range(1,N+1):
        # i행에서 mid보다 작거나 같은 숫자의 개수 
        # i행의 값들은 i*1, i*2, ... i*mid, ... 이기 때문에
        count += min(N, mid//i)
    
    # mid가 B[k]이려면 count k보다 작으면 안된다
    if count < k:
        l = mid
    else:
        r = mid 
    
print(r)
        

        

