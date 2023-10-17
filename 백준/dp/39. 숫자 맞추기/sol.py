import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100000)

n = int(input())
start,end = input()[:-1],input()[:-1]
dp = [dict() for _ in range(n)]

def track(depth, spin):
    if depth == n:
        return 0
    cur_v = (int(start[depth]) + spin) % 10
    tar_v = int(end[depth])
    if cur_v in dp[depth]:
        return dp[depth][cur_v][0]
    ans = None
    if tar_v == cur_v:
        ans = (track(depth+1,spin),0)
    else:
        l_spin = tar_v-cur_v if tar_v > cur_v else 10+tar_v-cur_v
        r_spin = tar_v-(10+cur_v) if tar_v > cur_v else tar_v-cur_v
        l_res = track(depth+1,spin+l_spin)
        r_res = track(depth+1,spin)
        if l_res+l_spin > r_res-r_spin:
            ans = (r_res-r_spin,r_spin)
        else:
            ans = (l_res+l_spin,l_spin)
    dp[depth][cur_v] = ans 
    return ans[0]

track(0,0)
spin = 0
print(dp[0][int(start[0])][0])
for i in range(n):
    cur_v = (int(start[i]) + spin) % 10
    cur_spin = dp[i][cur_v][1]
    print(i+1,cur_spin)
    spin += cur_spin if cur_spin > 0 else 0




    


