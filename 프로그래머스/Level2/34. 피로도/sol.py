
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    if n == 0:
        return 0
    else:
        for i in range(n):
            need_t, use_t = dungeons[i]
            if need_t > k:
                continue 
            else:
                temp = dungeons.copy()
                del temp[i]
                answer = max(solution(k-use_t,temp)+1,answer)

    return answer



print(solution(80	,[[80,20],[50,40],[30,10]]))