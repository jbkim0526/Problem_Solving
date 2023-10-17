
def solution(temp, t1, t2, a, b, onboard):
    answer = 0
    board,i = [],0
    n = len(onboard)
    while i < len(onboard):
        val = onboard[i]
        sindex = i
        while i < len(onboard) and onboard[i] == val:
            i += 1
        board.append((i-sindex,val))
    
    cur_temp = temp
    delta = -1 if temp > t2 else 1
    maintain = True if 2*b <= a else False
    n_board = len(board)

    def boardedUpper(cur_temp,length):
        energy = 0
        if cur_temp != t2:
            cur_temp = t2
            length -= t2-cur_temp
        if maintain:
            energy = b*length
            cur_temp = t2
        else:
            energy = a*(length//2) 
            cur_temp -= 1 if length % 2 else 0
        return energy, cur_temp

    def boardedLower(cur_temp,length):
        energy = 0
        if cur_temp != t1:
            cur_temp = t1
            length -= cur_temp-t1
        if maintain:
            energy = b*length
            cur_temp = t1
        else:
            energy = a*(length//2) 
            cur_temp += 1 if length % 2 else 0
        return energy, cur_temp

    def unboardedUpper(cur_temp,length):
        energies = []

        count = 2*temp-(cur_temp+t2)
        if count < length:
            activate_count = temp-t2
            energies.append((activate_count*a,t2))
        
        if maintain:
            activate_count = (cur_temp-t2)
            maintain_energy = a*(cur_temp-t2)+b*(length-activate_count)
            energies.append((maintain_energy,t2))
        
        length -= cur_temp-t2 
        activate_count = cur_temp-t2 + (length+1)//2
        cur_temp = t2-1 if length % 2 else t2
        energies.append((activate_count*a, cur_temp))
        energy,cur_temp = min(energies)
        return energy,cur_temp

    def unboardedLower(cur_temp,length):
        energies = []

        count = cur_temp+t1-2*temp
        if count < length:
            activate_count = t1-temp
            energies.append((activate_count*a,t1))

        if maintain:
            activate_count = t1-cur_temp
            maintain_energy = a*(t1-cur_temp)+b*(length-activate_count)
            energies.append((maintain_energy,t1))
        
        length -= t1-cur_temp 
        activate_count = t1-cur_temp + (length+1)//2
        cur_temp = t1+1 if length % 2 else t1
        energies.append((activate_count*a, cur_temp))
        energy,cur_temp = min(energies)
        return energy,cur_temp


    for i,(length, boarded) in enumerate(board):
        if i == n_board-1:
            if not boarded:
                return answer
            
        if temp > t2:
            if boarded:
                energy, new_temp = boardedUpper(cur_temp,length)
            else:
                energy, new_temp = unboardedUpper(cur_temp,length)
        else:
            if boarded:
                energy, new_temp = boardedLower(cur_temp,length)
            else:
                energy, new_temp = unboardedLower(cur_temp,length)
        answer += energy 
        cur_temp = new_temp

    return answer



print(solution(			11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))