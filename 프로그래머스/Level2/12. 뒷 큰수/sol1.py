def solution(numbers):
    answer = [-1]
    N = len(numbers)

    for i in reversed(range(N-1)):
        target = numbers[i]
        num_before = numbers[i+1]

        if target > num_before:
            for j in range(N-2-i,-1,-1):
                ans = answer[j]
                if ans > target:
                    answer.append(ans)
                    break 
                elif ans == -1 :
                    answer.append(-1)
                    break
            continue

        elif target == num_before:
            answer.append(answer[N-2-i])
            continue
        else:
            answer.append(num_before)
            continue

    answer.reverse()
    return answer

print(solution([9, 1, 5, 3, 6, 2]))