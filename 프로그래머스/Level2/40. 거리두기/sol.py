def isValid(r,c,place):

    checklist = [(0,-1),(0,1),(0,2),(1,-1),(1,0),(1,1),(2,0)]
    d = [""]*7
    for i,(dr,dc) in enumerate(checklist):
        if 4< r+dr or r+dr < 0 or 4 < c+dc or c+dc < 0:
            continue 
        d[i] = place[r+dr][c+dc]
        
    if d[1] =="P" or d[4] == "P":
        return False 
    if d[3] == "P" :
        if d[0] == "O" or d[4]  == "O":
            return False
    if d[6] == "P" and d[4]  == "O":
        return False
    if d[5] == "P":
        if d[1] ==  "O" or d[4] == "O":
            return False
    if d[2] == "P" and d[1] == "O":
        return False

    return True
    

def checkPlace(place):
    for row in range(5): 
        for col in range(5):
            if place[row][col] == "P" and not isValid(row, col, place):
                return False 
    return True

def solution(places):
    answer = []
    for place in places: 
        if checkPlace(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))