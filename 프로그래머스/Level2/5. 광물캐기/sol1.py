def getpicksNum(num_need, dia, iron, stone):
    dia_need = 0
    iron_need = 0 
    stone_need = 0
    if num_need > dia+iron+stone:
        dia_need = dia 
        iron_need = iron
        stone_need = stone 
    else:
        while num_need > 0:
            if dia_need == 0:
                if dia < num_need:
                    dia_need = dia
                    num_need -= dia
                else:
                    dia_need = num_need
                    num_need -= num_need 

            if iron_need == 0:
                if iron < num_need:
                    iron_need = iron
                    num_need -= iron
                else:
                    iron_need = num_need
                    num_need -= num_need   

            if stone_need == 0:
                if stone < num_need:
                    stone_need = stone
                    num_need -= stone
                else:
                    stone_need = num_need
                    num_need -= num_need 
    return dia_need , iron_need, stone_need

def solution(picks, minerals):
    answer = 0
    dia, iron, stone = picks
    pick_count = dia+iron+stone
    N = len(minerals)
    q = N // 5
    r = N % 5
    w = []

    if pick_count*5 > N: 
        for i in range(q):
            d_num = i_num = s_num = 0
            for j in range(5):
                if minerals[5*i+j] == "diamond":
                    d_num += 1
                elif minerals[5*i+j] == "iron":
                    i_num += 1 
                else:
                    s_num += 1
            d_t = d_num + i_num +s_num 
            i_t = 5*d_num + i_num +s_num 
            s_t = 25*d_num + 5*i_num +s_num 
            w.append((d_t,i_t,s_t))

        if r != 0:
            d_num = i_num = s_num = 0
            for j in range(r):
                if minerals[5*q+j] == "diamond":
                    d_num += 1
                elif minerals[5*q+j] == "iron":
                    i_num += 1 
                else:
                    s_num += 1
            d_t = d_num + i_num +s_num 
            i_t = 5*d_num + i_num +s_num 
            s_t = 25*d_num + 5*i_num +s_num 
            w.append((d_t,i_t,s_t))
    else:
        for i in range(pick_count):
            d_num = i_num = s_num = 0
            for j in range(5):
                if minerals[5*i+j] == "diamond":
                    d_num += 1
                elif minerals[5*i+j] == "iron":
                    i_num += 1 
                else:
                    s_num += 1
            d_t = d_num + i_num +s_num 
            i_t = 5*d_num + i_num +s_num 
            s_t = 25*d_num + 5*i_num +s_num 
            w.append((d_t,i_t,s_t))

    num_need = len(w)
    dia_need, iron_need, stone_need = getpicksNum(num_need, dia, iron, stone)
    w.sort(key= lambda x : -x[2])

    for i in range(dia_need):
        answer += w.pop(0)[0]
    for i in range(iron_need):
        answer += w.pop(0)[1]
    for j in range(stone_need):
        answer += w.pop(0)[2]
    return answer

solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])