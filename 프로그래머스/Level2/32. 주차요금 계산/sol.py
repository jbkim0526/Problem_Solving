from math import ceil

def getmin(s):
    h,m = map(int,s.split(":"))
    return 60*h+m

def solution(fees, records):
    answer = []


    basic_time, basic_fee, unit_time, unit_fee = fees
    in_dict = {}
    time_dict = {}

    for r in records:
        r_time, r_number, rp = r.split()
        r_time = getmin(r_time)
        if rp == "IN":
            in_dict[r_number] = r_time
        else:
            s_time = in_dict[r_number]
            del in_dict[r_number]
            if r_number in time_dict:
                time_dict[r_number] += r_time - s_time
            else:
                time_dict[r_number] = r_time - s_time

    for r_number,s_time in in_dict.items():
        if r_number in time_dict:
            time_dict[r_number] += 1439 - s_time
        else:
            time_dict[r_number] = 1439 - s_time
        

    l = list(time_dict.items())
    l.sort(key = lambda x: x[0])
    
    for _, time in l:
        if time < basic_time:
            answer.append(basic_fee)
        else:
            dt = ceil((time-basic_time) / unit_time)
            answer.append(basic_fee + unit_fee*dt)
            
    return answer




print(solution([180, 5000, 10, 600]	,["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))