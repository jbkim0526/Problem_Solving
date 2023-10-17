from math import inf

def solution(n, results):
    answer = 0
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for win,lose in results:
        dp[win-1][lose-1] = 1 
        dp[lose-1][win-1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] == 1 and dp[k][j] == 1:
                    dp[i][j] = 1
                elif dp[i][k] == -1 and dp[k][j] == -1:
                    dp[i][j] = -1

    for row in dp:
        if row.count(0) == 1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))