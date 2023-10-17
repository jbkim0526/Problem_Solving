import sys
input = sys.stdin.readline 

n = int(input()) 

R = []
G = []
B = []

for i in range(n):
    r,g,b = map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

DR = [R[0]] + [0]*(n-1)
DG = [G[0]] + [0]*(n-1)
DB = [B[0]] + [0]*(n-1)

for i in range(1,n):
    DR[i] = min(DG[i-1]+R[i], DB[i-1]+R[i])
    DG[i] = min(DR[i-1]+G[i], DB[i-1]+G[i])
    DB[i] = min(DG[i-1]+B[i], DR[i-1]+B[i])

print(min(DR[n-1],DG[n-1],DB[n-1]))