def maxSumIS(self, Arr, n):
    # code here


# i+1번째 수로 끝나는 증가 수열의 최대 합
    
    dp = [num for num in Arr]
    
    
    for i in range(1,n):
        for j in range(i):
            if Arr[j] < Arr[i]:
                dp[i] = max(dp[i],dp[j]+Arr[i])
                
    return max(dp)