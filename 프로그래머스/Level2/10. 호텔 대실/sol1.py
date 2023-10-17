def isOverlap(t1, t2):
    
    t1_end = t1[1]
    t2_start = t2[0]
    t1_m = int(t1_end[3:])+10
    t1_h = int(t1_end[0:2])
    if 70 > t1_m >= 60:
        t1_end = str(t1_h+1) + ":0" +str(t1_m - 60)
    else:
        t1_end = str(t1_h) + ":" +str(t1_m)
    return t1_end > t2_start


def solution(book_time):
    answer = 0

    book_time.sort(key = lambda x: x[0])
    current_rooms = []

    for new_time in book_time:
        room_available = False
        for i in range(len(current_rooms)):
            if not isOverlap(current_rooms[i], new_time):
                current_rooms[i] = new_time
                room_available = True 
                break
        if not room_available:
            current_rooms.append(new_time)
            answer += 1
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))