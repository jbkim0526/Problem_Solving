def sign(x):
    if x >= 0 : return x
    else: return 0

def get_cost(n_alp,n_cop,solvables):
    print(n_alp,n_cop)


    if n_alp <= 0 and n_cop <= 0:
        return 0,n_alp,n_cop
    l = []
    for g_alp, g_cop, used in solvables:

        if n_alp == 0 and g_cop == 0: continue 
        if n_cop == 0 and g_alp == 0: continue
        cost , c_alp, c_cop = get_cost(n_alp-g_alp, n_cop-g_cop, solvables)
        # 나중에 문제 될 수도
        l.append((used+cost,c_alp,c_cop))
    return min(l)

### 내생각엔 그냥 전부 재귀문을 돌려야 할 거 같음
### 돌리면서 solvable이랑 problems를 수정하고 
### 효율이 좋은 것을 선택, 만약 같다면 
### or DP???? -> 고려해보자
def solution(alp, cop, problems):
    answer = 0
    solvables = [(1,0,1),(0,1,1)]

    # 이미 풀수 있는 문제는 solvable로 옮기기
    for p in problems:
        if p[0] <= alp and p[1] <= cop:
            solvables.append((p[2],p[3],p[4]))
            problems.remove(p)

    # 풀 수 없는 문제를 하나씩 빼면서 solvable로 옮기기    
    while len(problems) > 0 :

        problems.sort(key = lambda x: -(sign(x[0]-alp)+sign(x[1]-cop)))
        p = problems.pop()
        while True:
            if p[0] > alp or p[1] > cop: break
            else: p = problems.pop()
    
        n_alp, n_cop = sign(p[0]-alp),sign(p[1]-cop)
        min_cost, c_alp, c_cop = get_cost(n_alp, n_cop, solvables)
        answer += min_cost 
        alp,cop = c_alp,c_cop

    return answer



print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))