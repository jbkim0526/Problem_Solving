def solution(routes):
    routes.sort(key = lambda x : (x[1],x[0]))
    answer = 0
    s = -30000
    for a,b in routes:
        if a > s:
            answer += 1
            s = b
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))