def time_convert(t):
    h,m = map(int, t.split(":"))
    return 60*h+m



def solution(book_time):
    answer = 0
    current_room = 0
    change_list = []

    for st, et in book_time:
        change_list.append((time_convert(st),1))
        change_list.append((time_convert(et)+10,-1))

    change_list.sort()

    for time, d in change_list:
        current_room += d
        if answer < current_room:
            answer = current_room 

    return answer 

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))