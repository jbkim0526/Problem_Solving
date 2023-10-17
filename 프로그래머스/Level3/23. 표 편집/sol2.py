def solution(n, k, cmd):
    row_info = ["O"]*n 
    erased = []
    for c in cmd:
        l = c.split(" ")
        op = l[0]
        if op in ["U","D"]:
            count = int(l[1])
            direction = 1 if op == "D" else -1
            while count > 0:
                k += direction
                if row_info[k] == "X":
                    continue 
                count -= 1
    
        elif op == "C":
            erased.append(k)
            row_info[k] = "X"
            for i in range(k,n):
                if row_info[i] == "X":
                    continue 
                k = i 
                break 
            else:
                for i in range(k,-1,-1):
                    if row_info[i] == "X":
                        continue
                    k = i 
                    break 
        else:
            row_info[erased.pop()] = "O"
    return ''.join(row_info)