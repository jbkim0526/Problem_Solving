def solution(order):
    answer = 0
    n = len(order)
    first_elem = order[0]

    aux_con = [i for i in range(1,first_elem)]
    origin_con = [i for i in reversed(range(first_elem,n+1))]

    for i in range(0,n):
        target = order[i]
        if len(origin_con) != 0 and target == origin_con[-1]:
            origin_con.pop()
            answer += 1
        elif len(aux_con) != 0 and target == aux_con[-1]:
            aux_con.pop()
            answer +=1
        else:
            if len(origin_con) == 0 or target < origin_con[-1]:
                break
            else:
                aux_con = aux_con + [i for i in range(origin_con[-1],target)]
                for i in range(target - origin_con[-1]+1):
                    origin_con.pop()
                answer += 1
    return answer



print(solution([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]))
