def solution(a, b, g, s, w, t):
    answer = 4*10**14
    left = 0
    right = 4*10**14
    len_cities = len(g)
    while left <= right:
        mid = (left+right)//2
        gold = 0 
        silver = 0
        total = 0
        for i in range(len_cities):
            cur_g,cur_s,cur_w,cur_t = g[i],s[i],w[i],t[i]
            count = mid // (cur_t*2) + (mid % (cur_t*2))//cur_t
            total_deliver_weight = count*cur_w
            gold += min(cur_g,total_deliver_weight)
            silver += min(cur_s,total_deliver_weight)
            total += min(cur_g+cur_s,total_deliver_weight)

        if gold >= a and silver >= b and total >= a+b:
            answer = min(mid, answer)
            right = mid-1
        else:
            left = mid + 1
    return answer

print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))