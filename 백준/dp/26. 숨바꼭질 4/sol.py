import sys 
input = sys.stdin.readline 

N, K =  map(int, input().split())
visited = set([N])
dp = {N:0}
cur_layer = [N]
depth = 1

while K not in visited:
    next_layer = []
    for cur_num in cur_layer:
        next_nums = [cur_num-1,cur_num+1,cur_num*2] if cur_num < K else [cur_num-1]
        for i,next_num in enumerate(next_nums):
            if next_num in visited:
                continue 
            if next_num < 0:
                continue
            visited.add(next_num)
            dp[next_num] = (depth,i)
            next_layer.append(next_num)
    cur_layer = next_layer
    depth += 1

ans = []
while True:
    ans.append(str(K))
    if K == N:
        break 
    t = dp[K][1]
    if t == 0:
        K += 1
    elif t == 1:
        K -= 1
    else:
        K //= 2
ans.reverse()
print(len(ans)-1)
print(" ".join(ans))
    


    
    
    



