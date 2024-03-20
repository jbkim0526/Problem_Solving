# 흔한 계단 오르기 문제
# 단 여기서는 바로 전 값만 필요하기 때문에 
# 추가적으로 메모리를 아낄 수 있다.

def minAmount(self, A, n): 
    # code here 
    
    dp1,dp2 = A[0],0
    for i in range (1,n):
        dp1,dp2 = min(dp1+A[i],dp2+A[i]),dp1
    
    return min(dp1,dp2)