import sys
from collections import deque
input = sys.stdin.readline 

ans = []
n, l = map(int, input().split())
numbers = list(map(int, input().split()))
inf = int(1e9)
tree = [inf]*n + numbers

for i in range(n-1,0,-1):
    tree[i] = min(tree[i<<1],tree[i<<1|1])

def tree_min(l,r):
	l+=n ; r+=n
	res = inf
	while l<r:
		if l&1:
			res = min(res,tree[l])
			l += 1
		if r&1:
			r -= 1
			res = min(res,tree[r])
		l>>=1; r>>=1
	return res

ans = []
d = deque()
cur_min = inf

for i in range(l):
    num = numbers[i]
    cur_min = min(cur_min,num)
    d.append(num)
    ans.append(str(cur_min))

for i in range(l,n):
    b_num = d.popleft()
    num = numbers[i]
    d.append(num)
    if b_num > cur_min:
        cur_min = min(cur_min,num)
        ans.append(str(cur_min))
    else:
        cur_min = tree_min(i-l+1,i+1)
        ans.append(str(cur_min))

print(" ".join(ans))



