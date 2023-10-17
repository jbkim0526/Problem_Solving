from collections import defaultdict

def toSecond(time):
    h,m,s = map(int,time.split(":"))
    return 3600*h+60*m+s

def toTimeString(time):
    t, s = divmod(time, 60)
    h, m= divmod(t, 60)
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)

def solution(play_time, adv_time, logs):
    play_time = toSecond(play_time)
    adv_time = toSecond(adv_time)
    start_times = defaultdict(int)
    end_times = defaultdict(int)
    people = [0]*play_time

    for log in logs:
        start_times[toSecond(log[:8])] += 1
        end_times[toSecond(log[9:])] += 1

    if 0 in start_times:
        people[0] = 1
    
    for i in range(1,play_time):
        people[i] += people[i-1]
        people[i] += start_times[i]
        people[i] -= end_times[i]
  
    range_sum = 0
    for i in range(adv_time):
        range_sum += people[i]

    max_range_sum = range_sum
    max_start_time = [0]

    for time in range(1,play_time-adv_time+1):
        range_sum -= people[time-1]
        range_sum += people[time+adv_time-1]
        if max_range_sum < range_sum:
            max_range_sum = range_sum
            max_start_time = [time]
        elif max_range_sum == range_sum:
            max_start_time.append(time)

    return toTimeString(max_start_time[0])


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
#print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
#print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))

#print(solution("25:00:00", "00:01:00", ["24:00:01-25:00:00"]))