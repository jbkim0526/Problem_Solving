from bisect import bisect_left

def solution(n, k, cmd):
    answer = ["X"]*n
    active_rows = [i for i in range(n)]
    erased = []
    end = n-1 
    for c in cmd:
        
        l = c.split(" ")
        op = l[0]
        if op in ["U","D"]:
            count = int(l[1])
            k += count if op == "D" else -count
        elif op == "C":
            erased.append(active_rows[k])
            del active_rows[k]
            if k == len(active_rows):
                k -= 1
        else:
            restore = erased.pop()
            i = bisect_left(active_rows,restore)
            if i <= k:
                k += 1
            active_rows.insert(i, restore)

    for i in active_rows:
        answer[i] ="O"
    
    return "".join(answer)

#print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(1000000, 9, ["D 100000", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))