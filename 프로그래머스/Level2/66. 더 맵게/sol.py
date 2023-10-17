from heapq import heappop, heappush


def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heappush(heap,s)
    while True:
        smallest = heappop(heap)
        if smallest >= K:
            break 
        if len(heap) == 0:
            return -1
        second_smallest = heappop(heap)
        heappush(heap, smallest+second_smallest*2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12]	,7))