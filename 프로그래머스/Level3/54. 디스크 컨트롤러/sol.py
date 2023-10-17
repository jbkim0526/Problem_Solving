def solution(jobs):
    answer = 0
    n = len(jobs)
    cur_time = 0
    jobs.sort(key = lambda x : -x[0])
    
    while len(jobs) > 0:
        startable_jobs = []
        while len(jobs) > 0:
            st,dt = jobs.pop()
            if st > cur_time:
                jobs.append([st,dt])
                break 
            startable_jobs.append([st,dt])

        if len(startable_jobs) == 0:
            st,dt = jobs.pop()
            answer += dt
            cur_time = st+dt
            continue

        st,dt = min(startable_jobs,key = lambda x : x[1])
        cur_time += dt
        answer +=  cur_time - st
        startable_jobs.remove([st,dt])
        for job in reversed(startable_jobs):
            jobs.append(startable_jobs.pop())
    
    return int(answer/n)


print(solution(	[[0, 3], [11, 9], [2, 6]]))