def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker[0],sticker[1])
    dp1 = [0]*n
    dp2 = [0]*n

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2,n-1):
        dp1[i] = max(dp1[i-1],dp1[i-2]+sticker[i])
        dp2[i] = max(dp2[i-1],dp2[i-2]+sticker[i])
    
    dp2[n-1] = max(dp2[n-2],dp2[n-3]+sticker[n-1])
    return max(dp1[n-2],dp2[n-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))