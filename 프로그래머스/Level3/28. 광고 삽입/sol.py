def toSecond(time):
    h,m,s = map(int,time.split(":"))
    return 3600*h+60*m+s


def solution(play_time, adv_time, logs):
    answer = ''
    play_time = toSecond(play_time)
    adv_time = toSecond(adv_time)
    times = []
    for log in logs:
        starttime = toSecond(log[:8])
        endtime = toSecond(log[9:])
        times.append((starttime,1))
        times.append((endtime,-1))
    times.sort(key = lambda x: x[0])
    

    people = [0]*play_time

    for i in range(play_time):
        if i 
        people[i] = people


    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
print(toSecond("99:59:59"))