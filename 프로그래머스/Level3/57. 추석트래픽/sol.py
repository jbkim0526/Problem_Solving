from collections import deque,defaultdict
def parseLine(line):
    l = line.split(" ")
    h,m,s = l[1].split(":")
    etime = 3600*1000*int(h) + 60*1000*int(m) + int(1000*float(s))
    duration = int(1000*float(l[2][:-1]))
    return etime, duration

def solution(lines):
    answer = 0
    times = []
    
    for line in lines:
        etime, duration = parseLine(line)
        stime = etime-duration+1
        times.append((stime,etime))

    min_stime = min(times,key= lambda x: x[0])[0]
    max_etime = max(times,key= lambda x: x[1])[1]
    
    if (max_etime-min_stime+1) < 1000:
        return len(lines)
    
    instant_throughput = defaultdict(int)
    range_throughput = defaultdict(int)

    for stime,etime in times:
        instant_throughput[stime] += 1
        if etime+1 >= 86399999:
            continue
        instant_throughput[etime+1] -= 1 

    print(instant_throughput)

    return 


print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))