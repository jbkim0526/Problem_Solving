def parseLine(line):
    l = line.split(" ")
    h,m,s = l[1].split(":")
    etime = 1000*(3600*int(h)+60*int(m))+int(1000*float(s))
    duration = int(1000*float(l[2][:-1]))
    return etime, duration

def solution(lines):
    answers = []
    times = []
    for line in lines:
        etime, duration = parseLine(line)
        stime = etime-duration+1
        times.append((max(0,stime-999),1))
        times.append((min(86399999,etime+1),-1))
    
    times.sort(key = lambda x: x[0])
    if (times[-1][0]-(times[0][0]+999)+1) < 1000:
        return len(lines)
    cur_throughput = 0
    for time, val in times:
        cur_throughput += val
        answers.append(cur_throughput)
    return max(answers)

print(solution(	["2016-09-15 00:00:00.000 3s"]))
#print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))