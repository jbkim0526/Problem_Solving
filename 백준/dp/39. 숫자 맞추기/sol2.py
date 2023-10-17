import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100000)

def sol2(n,start,end):
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
        if cur_spin != 0:
            print(i+1,cur_spin)
        spin += cur_spin


def sol(N,A,B):
  DP = [[float("inf")] * 10 for _ in range(N+1)]
  DP[0] = [*range(10)]
  DP2 = [[None] * 10 for _ in range(N)] #회전량

  for i, (a, b) in enumerate(zip(A, B)):
    for j in range(10) :
      l = (b - a - j) % 10 #(현재 상태에서 B에 맞추기 위해)왼쪽으로 회전해야 하는 횟수
      r = 10 - l #오른쪽으로 회전해야 하는 횟수
      if DP[i+1][j] > DP[i][j] + r : #오른쪽으로 돌린 경우가 더 적은 경우
        DP[i+1][j] = DP[i][j] + r 
        DP2[i][j] = -r

      if DP[i+1][(j + l) % 10] > DP[i][j] + l : #왼쪽으로 돌린 경우가 더 적은 경우
        DP[i+1][(j + l) % 10] = DP[i][j] + l
        DP2[i][(j + l) % 10] = l

  answer = float("inf")
  for i, v in enumerate(DP[N]) :
    if answer > v :
      answer = min(answer, v)
      cur = i
  
  sys.stdout.write(str(answer) + "\n")
  answer = []
  for i in range(N-1, -1, -1) : #음수면 그대로 위칸, 양수면 -N칸
    answer.append(DP2[i][cur])
    if DP2[i][cur] < 0 : continue
    cur = (cur - DP2[i][cur]) % 10
  
  for i, v in enumerate(answer[::-1]) :
    sys.stdout.write(str(i+1) + " " + str(v) + "\n")

# 길이 3 테스트
for num in range(100,999):
    for num2 in range(100,999):
        
        n1 = str(num)
        n2 = str(num2)
        print("-----"+n1+" "+n2+"-----")
        sol2(3,n1,n2)
        print(" ")
        sol(3,[*map(int, n1)],[*map(int, n2)])



    


