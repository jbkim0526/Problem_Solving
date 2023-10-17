from itertools import permutations
from collections import deque

def operate(a,op,b):
    if op == "-":
        return a-b 
    elif op == "*":
        return a*b
    else: 
        return a+b 


def solution(expression):
    answer = 0
    operators = ["-","*","+"]
    main_d = deque()
    num_index = 0

    for i in range(len(expression)):
        if expression[i] in operators:
            main_d.append(int(expression[num_index:i]))
            main_d.append(expression[i])
            num_index = i+1
    main_d.append(int(expression[num_index:]))
    operators = list(permutations(operators,3))

    for operator in operators:
        d = main_d.copy()
        for i in range(3):
            target_op = operator[i]
            while len(d) > 1:
                n1,op,n2 = d.popleft(),d.popleft(),d.popleft()
                if isinstance(op, int):
                    d.append(n1); d.appendleft(n2); d.appendleft(op)         
                    break
                if op == target_op:
                    d.appendleft(operate(n1,op,n2))
                else:
                    d.append(n1); d.append(op); d.appendleft(n2)

        answer = max(abs(d.pop()),answer)

    return answer


print(solution("100-200*300-500+20"))