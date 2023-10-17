def solution(n, stations, w):
    answer = 0
    cur_status = 0 
    start_index = 0
    indexs = []
    need_ranges = []

    for station in stations:
        index = station-1 
        sindex,eindex = index-w,index+w
        indexs.append((max(0,sindex),1))
        indexs.append((eindex+1,-1))

    indexs.sort(key = lambda x : x[0])
    for index,val in indexs:
        if index > n-1: 
            continue
        if val == 1:
            if cur_status == 0 and index:
                need_ranges.append([start_index,index-1])
            cur_status += 1
        else:
            cur_status -= 1
            if cur_status == 0:
                start_index = index 

    if cur_status == 0:
        need_ranges.append([start_index,n-1])

    for a,b in need_ranges:
        answer += (b-a+1)//(2*w+1) + (1 if (b-a+1)%(2*w+1) else 0)
    return answer




#print(solution(6,[3],2))
print(solution(11, [4,11], 1))