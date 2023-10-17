def timedif(t1,t2):
    hdif = int(t2[0:2])-int(t1[0:2])
    return 60*hdif + int(t2[3:])-int(t1[3:])


def solution(plans):
    answer = []
    waiting = []
    time = ""
    now = None
    plans.sort(key= lambda x : x[1])
    
    while len(plans) > 0 or len(waiting) > 0:
        if not now:
            name, start, duration = plans.pop(0)
            time = start
            now = (name,int(duration))
        else:
            if len(plans) > 0:
                nxtname, nxtstart, nxtduration = plans.pop(0)
                td = timedif(time, nxtstart)
                curduration = now[1]
                if td < curduration:
                    waiting.append((now[0], curduration - td))
                    time = nxtstart
                    now = (nxtname, int(nxtduration))
                elif td == curduration:
                    answer.append(now[0]) 
                    time = nxtstart
                    now = (nxtname, int(nxtduration)) 
                else:
                    answer.append(now[0])
                    gap = td - curduration
                    while len(waiting) > 0 and gap > 0:
                        wtname, wtduration = waiting.pop(-1)
                        if gap >= wtduration:
                            answer.append(wtname)
                            gap -= wtduration
                        else:
                            waiting.append((wtname,wtduration-gap))
                            gap = 0
                    time = nxtstart
                    now = (nxtname,int(nxtduration))
            else:
                if now: 
                    answer.append(now[0])
                    now = None
                while len(waiting)>0:
                    answer.append(waiting.pop(-1)[0])
    if now:
        answer.append(now[0])
    return answer


a = solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])
print(a)