from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    heap = []

    for cur_enemy in enemy:
        heappush(heap,-1*cur_enemy)
        n -= cur_enemy

        if n < 0:
            if k == 0:
                return answer
            max_num = -1*heappop(heap)
            n += max_num
            k -= 1
        answer += 1

    return answer