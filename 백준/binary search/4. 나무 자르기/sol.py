import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int,input().split()))

l = -1
r = 1000000001


def tree_length(h):
    total = 0
    for tree in trees:
        total += tree-h if h < tree else 0        
    return total


while l+1 < r:
    mid = (l+r)//2
    if tree_length(mid) >= M:
        l = mid 
    else:
        r = mid

print(l)
