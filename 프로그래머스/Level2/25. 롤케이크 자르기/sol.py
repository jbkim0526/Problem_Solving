from collections import defaultdict

def solution(topping):
    answer = 0

    original_stack = defaultdict(int)
    current_stack = defaultdict(int)

    for num in topping:
        original_stack[num] += 1

    for num in topping:
        current_stack[num] += 1
        original_stack[num] -= 1
        if original_stack[num] == 0:
            del original_stack[num]
        if len(current_stack) == len(original_stack):
            answer += 1
    
    return answer

print(solution([1, 2, 3, 1, 4]))