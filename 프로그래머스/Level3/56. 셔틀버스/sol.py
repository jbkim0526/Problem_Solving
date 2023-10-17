def toMinute(time):
    return 60*int(time[0:2])+int(time[3:5])

def toStr(time):
    return str(time // 60).zfill(2)+":"+str(time % 60).zfill(2)
    

def solution(n, t, m, timetable):
    
    crew_times = []
    for time in timetable:
        crew_times.append(toMinute(time))
    crew_times.sort(reverse= True)
    last_bus_time = 540+t*(n-1)
    print(last_bus_time)
    print(crew_times)
    for i in range(n-1):
        bus_time = 540 + t*i
        for _ in range(m):
            if len(crew_times) == 0:
                return toStr(last_bus_time)
            ctime = crew_times.pop()
            if ctime > bus_time:
                crew_times.append(ctime)
                break

    for _ in range(m-1):
        if len(crew_times) == 0:
            return toStr(last_bus_time)
        ctime = crew_times.pop()
        if ctime > last_bus_time:
            crew_times.append(ctime)
            break
    else:
        if len(crew_times) == 0:
            return toStr(last_bus_time)
        ctime = crew_times.pop()
        if ctime > last_bus_time:
            return toStr(last_bus_time)
        return toStr(ctime-1)
    return toStr(last_bus_time)

print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))