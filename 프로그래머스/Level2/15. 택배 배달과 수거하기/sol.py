# 가장 먼 곳 부터 해결
def remove_box(house_pos, house_box_counts, cap, move_left):
    
    # 트럭에 실을 box의 개수
    box_count = min(move_left,cap)

    while box_count > 0 and move_left:
        house_num = house_pos[-1] - 1
        house_box_count = house_box_counts[house_num] 
 
        if house_box_count > box_count:
            house_box_counts[house_num] -= box_count
            move_left -= box_count
            box_count = 0
        else:
            box_count -= house_box_count
            move_left -= house_box_count
            house_box_counts[house_num] = 0
            house_pos.pop()

    return move_left


def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_pos, pickup_pos = [],[]

    for i in range(n):
        if deliveries[i] != 0 :
            delivery_pos.append(i+1)
        if pickups[i] != 0:
            pickup_pos.append(i+1)

    delivery_left = sum(deliveries)
    pickup_left = sum(pickups)

    while delivery_left or pickup_left:
        if delivery_left and pickup_left:
            max_pos = max(delivery_pos[-1],pickup_pos[-1])
            delivery_left = remove_box(delivery_pos,deliveries,cap, delivery_left)
            pickup_left = remove_box(pickup_pos, pickups, cap, pickup_left)
        elif delivery_left:
            max_pos = delivery_pos[-1]
            delivery_left = remove_box(delivery_pos,deliveries,cap, delivery_left)
        else:
            max_pos = pickup_pos[-1]
            pickup_left = remove_box(pickup_pos, pickups, cap, pickup_left)
        
        answer += 2*max_pos

    return answer


#print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
#print(solution(	4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 2, [0,0], [0,4]))