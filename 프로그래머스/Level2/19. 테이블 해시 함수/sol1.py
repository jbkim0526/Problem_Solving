from functools import reduce
def solution(data, col, row_begin, row_end):
    data.sort(key= lambda x : (x[col-1],-x[0]))
    si_list = []
    for i in range(row_begin-1, row_end):
        si = 0
        for elem in data[i]:
            si += elem % (i+1) 
        si_list.append(si)
    
    answer = si_list[0]
    for i in range(1, len(si_list)):
        answer ^= si_list[i]

    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],	2	,2	,3))