# 이거만 짜면 끝
def find_indices(lst, cap):
    result = []
    return result 


def solution(cap, n, deliveries, pickups):
    answer = 0
    dcount = []
    pcount = []
    dcap = cap
    pcap = cap

    dcount = find_indices(deliveries,cap)
    pcount = find_indices(pickups, cap)

    while len(dcount) > 0 or len(pcount)>0:
        if len(dcount) == 0:
            answer += sum(pcount)
            break
        elif len(pcount) == 0:
            answer += sum(dcount)
            break 
        else: 
            dv = dcount.pop(0)
            pv = pcount.pop(0)
            answer += max(dv,pv)

    return 2*answer


#print(solution(10,10	,[100,0,0,0,0,0,0,0,0,0],	[0, 0,0,0,0,0, 0,0,0,10]))
