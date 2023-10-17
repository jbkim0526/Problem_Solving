def solution(n, works):
    answer = 0
    len_works = len(works)
    total_works = sum(works) - n
    if total_works <= 0:
        return answer 

    q = total_works // len_works
    works.sort(reverse= True)
    table = []
    
    end = len_works
    for i in range(len_works):
        if q >= works[i]:
            end = i 
            break
        table.append(q)
        total_works -= q
    
    for i in range(end,len_works):
        table.append(works[i])
        total_works -= works[i]

    while total_works > 0:
        end -= 1
        num = works[end]-table[end] 
        if total_works >= num*(end+1):
            for i in range(end+1):
                table[i] += num 
            total_works -= num*(end+1)
        else:
            break

    while total_works > 0:
        for i in range(len_works):
            if works[i] == table[i] or total_works == 0:
                break
            table[i] += 1
            total_works -= 1

    for num in table:
        answer += num**2
    return answer

print(solution(		4, [4, 3, 3]))