import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100000)
n = int(input())

start = input()[:-1]
end = input()[:-1]

dp = [dict() for _ in range(n)]
spin = 0

def track(depth, spin):
    if depth == n:
        return 0
    cur_v = (int(start[depth]) + spin) % 10
    tar_v = int(end[depth])
    if cur_v in dp[depth]:
        return dp[depth][cur_v]
    ans = 0
    if tar_v == cur_v:
        ans = track(depth+1,spin)
    elif tar_v > cur_v:
        l_spin = spin + tar_v - cur_v
        ans = min(track(depth+1, l_spin)+ tar_v-cur_v, track(depth+1,spin)+ 10+cur_v-tar_v)
    else:
        l_spin = spin + 10+tar_v-cur_v
        ans = min(track(depth+1, spin)+ cur_v-tar_v, track(depth+1,l_spin)+ 10+tar_v-cur_v)

    dp[depth][cur_v] = ans 
    return ans

track(0,0)
print(dp[0][int(start[0])])


    


