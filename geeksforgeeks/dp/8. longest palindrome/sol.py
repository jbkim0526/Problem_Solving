def longestPalindrome(self, S):

    size = len(S)
    
    dp = [[0 for _ in range(size)] for _ in range(size)]
    max_len,ri,rj = 1, 0,0 
    
    # 초기값 설정
    for i in range(size):
        dp[i][i] = 1
    
        # 좌축 확인
        if i-1 >= 0 and S[i-1] == S[i]:
            dp[i-1][i] = 1
            if max_len < 2:
                max_len,ri,rj = 2,i-1,i
        
        # 우측확인
        if i+1 <= size-1 and S[i+1] == S[i]:
            dp[i][i+1] = 1
            if max_len < 2:
                max_len,ri,rj = 2,i,i+1 
        
        # 양쪽확인
        if i-1 >= 0 and i+1 <= size-1 and S[i+1] == S[i-1]:
            dp[i-1][i+1] = 1
            if max_len < 3:
                max_len,ri,rj = 3,i-1,i+1
                
    for l in range(2,size+1):
        for i in range(size-l+1):
            if not dp[i][i+l-1]: 
                continue
            
            if i-1 >= 0 and i+l <= size-1 and S[i-1] == S[i+l]:
                dp[i-1][i+l] = 1
                if max_len < l+2:
                    max_len,ri,rj = l+2,i-1,i+l
                    
    return S[ri:rj+1]