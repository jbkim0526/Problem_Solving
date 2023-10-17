from collections import deque

def solution(bridge_length, weight, truck_weights):

    trucks = deque(truck_weights)
    bridge = deque()
    time = 0
    current_weight = 0
    while len(trucks) > 0:
        w = trucks.popleft()
        if current_weight + w > weight:
            tw, end_time = bridge.popleft()
            current_weight -= tw
            time = end_time
            if current_weight + w <= weight:
                bridge.append((w, end_time + bridge_length))
                current_weight += w
            else:
                trucks.appendleft(w)
        else:
            bridge.append((w, time + 1 + bridge_length))
            current_weight += w
            time += 1
            if bridge[0][1] == time :
                current_weight -= bridge.popleft()[0]
    return bridge[-1][1]

print(solution(5, 5, [2,2,2,2,1,1,1,1,1]))