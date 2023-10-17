import sys
input = sys.stdin.readline

n = int(input())
l  = []
for i in range(n):
    l.append(int(input()))

if n == 1:
    print(l[0])
else:
    dp_1 = [l[0],l[0]+l[1]]+[0]*(n-2)
    dp_2 = [0,l[1]]+[0]*(n-2)

    for i in range(2,n):
        dp_1[i] = dp_2[i-1]+l[i]
        dp_2[i] = max(dp_1[i-2]+l[i], dp_2[i-2]+l[i])

    print(max(dp_1[-1],dp_2[-1]))