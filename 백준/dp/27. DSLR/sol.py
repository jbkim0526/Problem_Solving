import sys 
input = sys.stdin.readline 

def shift(x,t):
    s = str(x).zfill(4)
    res = s[-1]+s[0:-1] if t else s[1:]+s[0]
    return int(res)

for _ in range(int(input())):

    N,K = map(int, input().split())
    visited = set([N])
    dp = dict()
    layer = [N]
    while K not in visited:
        new_layer = []
        for num in layer:
            next_nums = [(2*num)%10000,(num-1)%10000,shift(num,0),shift(num,1)]
            for i,next_num in enumerate(next_nums):
                if next_num in visited:
                    continue 
                visited.add(next_num)
                dp[next_num] = (i,num)
                new_layer.append(next_num)
        layer = new_layer

    cur_num = K 
    op_list = ["D","S","L","R"]
    ans = []
    while cur_num != N:
        op, before_num = dp[cur_num]    
        ans.append(op_list[op])
        cur_num = before_num
    ans.reverse()
    print("".join(ans))

