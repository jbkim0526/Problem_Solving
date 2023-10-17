import sys 
input = sys.stdin.readline 


r,c,m = map(int,input().split())
sharks= []
for _ in range(m):
    sharks.append(list(map(int,input().split())))

def moveshark(shark):
    i,j,s,d,_ = shark
    new_shark = shark.copy()

    if d == 1:
        if s <= i-1:
            new_shark[0] = i-s
            return new_shark
        s -= i-1
        quo,rem = s // (r-1), s % (r-1)
        if quo % 2 == 0:
            new_shark[0] = rem 
            if rem ==0 : new_shark[3] = 1
            else: new_shark[3] = 2
        else:
            new_shark[0] = r-rem
            if rem ==0 : new_shark[3] = 2
            else: new_shark[3] = 1

    if d == 1:
        if s <= i-1:
            new_shark[0] = i-s 
            return new_shark 
        s -= i-1
        quo,rem = s // (r-1), s % (r-1)

        if rem:
            
        else:
            if quo % 2 :
                
            new_shark[0] = 1


        if quo % 2 == 0:
            if rem == 0:

            new_shark[0] = rem 



for shark in sharks:
    print(moveshark(shark))

        
