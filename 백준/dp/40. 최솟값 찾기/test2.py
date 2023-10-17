arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0]*(len(arr)) + arr
inf = int(1e9)
n = len(arr)
for i in range(n-1,0,-1):
    tree[i] = min(tree[i<<1],tree[i<<1|1])

def query(l,r):
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

print(query(5,8))