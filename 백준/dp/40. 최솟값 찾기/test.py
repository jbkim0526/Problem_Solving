arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (len(arr) * 4)
inf = int(1e9)
def init(start,end,node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = min(init(start,mid,node*2),init(mid+1,end,node*2+1))
    return tree[node]

def tree_min(start,end,node,left,right):

    if left > end or right < start: 
        return inf
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start+end)//2
    return min(tree_min(start,mid,2*node,left,right),tree_min(mid+1, end, 2*node+1, left, right))


init(0,len(arr)-1,1)

print(tree)
print(tree_min(0,len(arr)-1,1,1,5))

