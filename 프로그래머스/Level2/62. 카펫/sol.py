def solution(brown, yellow):
    answer = []
    wph = (brown+4)//2 
    wh = yellow + brown
    t = int((wph*wph - 4*wh)**(1/2))
    answer = [(wph + t)//2,(wph - t)//2]
    return answer

print(solution(10,2))