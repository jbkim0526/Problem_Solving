from heapq import heapify, heappop, heappush


def solution(operations):
    answer = []
    max_heap = []
    min_heap = []

    for operation in operations:
        if operation[0] == "I":
            num = int(operation[2:])
            heappush(min_heap, num)
            heappush(max_heap, -num)
        
        elif operation[2:] == "1":
            if len(max_heap) == 0:
                continue
            val = -heappop(max_heap)
            min_heap.remove(val)
            heapify(min_heap)
        else:
            if len(min_heap) == 0:
                continue
            val = heappop(min_heap)
            max_heap.remove(-val)
            heapify(max_heap)

    if len(max_heap) == 0:
        answer.append(0)
    else:
        answer.append(-max_heap[0]) 
    if len(min_heap) == 0:
        answer.append(0)
    else:
        answer.append(min_heap[0])
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))