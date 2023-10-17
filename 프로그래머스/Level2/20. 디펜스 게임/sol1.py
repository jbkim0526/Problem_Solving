def solution(n, k, enemy):
    answer = 0

    dp = [enemy[0], 0]
    enemies = len(enemy)
    if enemies <= k:
        answer = enemies
        return answer

    for i in range(1, enemies):
        # i+1 round
        temp = []
        enemy_num = enemy[i]
        # j : 0 ~ min(i+1,k) 
        m = min(i+2,k+1)
        for j in range(0,m):
            if j == 0:
                temp.append(dp[0]+enemy_num)
            elif j == i+1:
                temp.append(0)
            else:
                temp.append(min(dp[j-1],dp[j]+enemy_num))
        if m == k+1 and temp[k] > n:
            answer = i
            return answer
        dp = temp

    return answer

print(solution(2,3,	[3,3,3,3])) 



""" 
테스트 1 〉	통과 (521.86ms, 10.4MB)
테스트 2 〉	통과 (3201.66ms, 11.2MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	통과 (0.00ms, 10.5MB)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	통과 (1.56ms, 18.7MB)
테스트 12 〉	통과 (14.83ms, 18.5MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	실패 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.00ms, 10.1MB)
테스트 19 〉	실패 (0.01ms, 10.3MB)
테스트 20 〉	실패 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.00ms, 10.1MB)
테스트 23 〉	통과 (0.48ms, 10.3MB)
테스트 24 〉	통과 (0.50ms, 10.1MB)
테스트 25 〉	통과 (0.33ms, 10.2MB)
테스트 26 〉	통과 (1.93ms, 10.2MB)
테스트 27 〉	통과 (1.27ms, 10.3MB)
테스트 28 〉	통과 (0.54ms, 10.3MB)
테스트 29 〉	실패 (4.66ms, 10.1MB)
테스트 30 〉	통과 (0.94ms, 10.2MB)
테스트 31 〉	통과 (2.67ms, 10.2MB)
테스트 32 〉	통과 (2.02ms, 10.3MB)
"""