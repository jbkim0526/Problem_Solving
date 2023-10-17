def solution(topping):
    answer = 0

    original_stack = {}
    current_stack = {}

    for i in topping:
        if not i in original_stack:
            original_stack[i] = 1
        else:
            original_stack[i] += 1

    for i in topping:
        if not i in current_stack:
            current_stack[i] = 1
        else:
            current_stack[i] += 1
        original_stack[i] -= 1
        if original_stack[i] == 0:
            del original_stack[i]
        if len(current_stack) == len(original_stack):
            answer += 1
    
    return answer

print(solution([1, 2, 3, 1, 4]	))