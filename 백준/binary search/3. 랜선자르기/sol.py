import sys 
input = sys.stdin.readline 

K, N = map(int,input().split())
lines = [int(input()[:-1]) for _ in range(K)]

l = 0
r = 2**31

def count_line(length):
    count = 0
    for line in lines:
        count += line // length
    return count

while l+1 < r:
    mid = (l+r)//2
    if count_line(mid) >= N:
        l = mid 
    else:
        r = mid

print(l)
