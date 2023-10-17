def solution(commands):
    answer = []

    table = [["" for _ in range(50)] for _ in range(50)]
    merge_dict = {}

    for command in commands:
        c = list(command.split())
        op = c[0]
        if op == "UPDATE":
            if len(c) == 4:
                r,c,value = int(c[1])-1,int(c[2])-1,c[3]
                if (r,c) in merge_dict:
                    s = merge_dict[(r,c)]
                    for _r,_s in s:
                        table[_r][_s] = value
                else: table[r][c] = value
            else:
                val1,val2 = c[1],c[2]
                for i in range(50):
                    for j in range(50):
                        if table[i][j] == val1:
                            table[i][j] = val2
                    
        elif op == "MERGE":
            r1,c1,r2,c2 = int(c[1])-1,int(c[2])-1,int(c[3])-1,int(c[4])-1
            if (r1,c1) == (r2,c2):
                continue

            v1 = table[r1][c1] ; v2 = table[r2][c2] ; v = ""
            if v1 == "" and v2 != "": v = v2
            else: v = v1 

            if (r1,c1) in merge_dict and (r2,c2) in merge_dict:
                s1 = merge_dict[(r1,c1)]
                s2 = merge_dict[(r2,c2)]
                for r,c in s2:
                    s1.add((r,c))
                    merge_dict[(r,c)] = s1
                for r,c in s1:
                    table[r][c] = v
            elif (r1,c1) in merge_dict:
                s1 = merge_dict[(r1,c1)]
                s1.add((r2,c2))
                merge_dict[(r2,c2)] = s1
                for r,c in s1:
                    table[r][c] = v
            elif (r2,c2) in merge_dict:
                s2 = merge_dict[(r2,c2)]
                s1 = set([(r1,c1)])
                merge_dict[(r1,c1)] = s1
                for r,c in s2:
                    s1.add((r,c))
                    merge_dict[(r,c)] = s1
                for r,c in s1:
                    table[r][c] = v
            else:
                table[r1][c1] = v ; table[r2][c2] = v
                s = set([(r1,c1),(r2,c2)])
                merge_dict[(r1,c1)] = s 
                merge_dict[(r2,c2)] = s

        elif op == "UNMERGE":
            r,c = int(c[1])-1,int(c[2])-1
            v = table[r][c]
            if (r,c) in merge_dict:
                for _r,_s in merge_dict[(r,c)]:
                    table[_r][_s] = ""
                    del merge_dict[(_r,_s)]
                table[r][c] = v
     
        else:
            r,c = int(c[1])-1,int(c[2])-1
            v = table[r][c]
            if v == "": answer.append("EMPTY")
            else: answer.append(v)

    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))