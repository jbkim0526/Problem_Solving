import sys 

input = sys.stdin.readline
n, m = map(int, input().split())
b = [list(map(int,input().split())) for _ in range(n)]


def check_square(i,j):
    ni,nj = i+1,j+1
    if ni > n-1 or nj > m-1:
        return 0    
    return b[i][j]+b[ni][j]+b[i][nj]+b[ni][nj]

def check_line(i,j):
    ans = 0
    if i+3 <= n-1:
        ans = max(ans, b[i][j]+b[i+1][j]+b[i+2][j]+b[i+3][j])
    if j+3 <= m-1:
        ans = max(ans, b[i][j]+b[i][j+1]+b[i][j+2]+b[i][j+3])
    return ans 

def check_l(i,j):
    ans = [0]
    if i+1 <= n-1 and j+2<= m-1:
        ans.append(b[i][j]+b[i+1][j]+b[i][j+1]+b[i][j+2])
        ans.append(b[i][j]+b[i+1][j+2]+b[i][j+1]+b[i][j+2])
    if i-1 >= 0 and j-2 >= 0:
        ans.append(b[i][j]+b[i-1][j]+b[i][j-1]+b[i][j-2])
        ans.append(b[i][j]+b[i-1][j-2]+b[i][j-1]+b[i][j-2])
    if i+2 <= n-1 and j-1 >= 0:
        ans.append(b[i][j]+b[i][j-1]+b[i+1][j]+b[i+2][j])
        ans.append(b[i][j]+b[i+2][j-1]+b[i+1][j]+b[i+2][j])
    if i-2 >= 0 and j+1 <= m-1:
        ans.append(b[i][j]+b[i][j+1]+b[i-1][j]+b[i-2][j])
        ans.append(b[i][j]+b[i-2][j+1]+b[i-1][j]+b[i-2][j])
    return max(ans)

def check_f(i,j):
    ans = [0]
    if i-1 >= 0 and j+1 <= m-1 and j-1 >= 0:
        ans.append(b[i][j]+b[i-1][j]+b[i][j+1]+b[i][j-1])
    if i+1 <= n-1 and j+1 <= m-1 and j-1 >= 0:
        ans.append(b[i][j]+b[i+1][j]+b[i][j+1]+b[i][j-1])
    if i+1 <= n-1 and i-1 >= 0 and j+1 <= m-1:
        ans.append(b[i][j]+b[i+1][j]+b[i-1][j]+b[i][j+1])
    if i+1 <= n-1 and i-1 >= 0 and j-1 >= 0:
        ans.append(b[i][j]+b[i+1][j]+b[i-1][j]+b[i][j-1])
    return max(ans)

def check_r(i,j):
    ans = [0]
    if i+1 <= n-1 and j+1 <= m-1 and j-1 >= 0:
        ans.append(b[i][j]+b[i][j-1]+b[i+1][j]+b[i+1][j+1])
        ans.append(b[i][j]+b[i][j+1]+b[i+1][j]+b[i+1][j-1])
    if i-1 >= 0  and i+1 <= n-1 and j+1 <= m-1:
        ans.append(b[i][j]+b[i][j+1]+b[i+1][j]+b[i-1][j+1])
        ans.append(b[i][j]+b[i-1][j]+b[i][j+1]+b[i+1][j+1])
    return max(ans)



ans = []
for i in range(n):
    for j in range(m):
        ans.append(check_square(i,j))
        ans.append(check_line(i,j))
        ans.append(check_l(i,j))
        ans.append(check_r(i,j))
        ans.append(check_f(i,j))
print(max(ans))

