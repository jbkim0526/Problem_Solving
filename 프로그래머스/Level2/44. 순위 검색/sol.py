def solution(info, query):
    answer = []

    table = [[[[[] for _ in range(2)] for _ in range(2)]for _ in range(2)] for _ in range(3)]
    d = {"cpp":0, "java":1,"python":2, "backend":0, "frontend":1 ,"junior":0, "senior":1, "chicken":0, "pizza": 1}


    def f(lan, job, time, food ,score, depths):
        count = 0
        if depths == 0:
            if lan == "-":
                for i in range(3):
                    count += f(i,job,time,food,score,1)
            else:
                count += f(d[lan],job,time,food,score,1)

        elif depths == 1:
            if job == "-":
                for i in range(2):
                    count += f(lan,i,time,food,score,2)
            else:
                count += f(lan,d[job],time,food,score,2)
        
        elif depths == 2:
            if time == "-":
                for i in range(2):
                    count += f(lan,job,i,food,score,3)
            else:
                count += f(lan,job,d[time],food,score,3)
        
        elif depths == 3:
            if food == "-":
                for i in range(2):
                    count += f(lan,job,time,i,score,4)
            else:
                count += f(lan,job,time,d[food],score,4)    
        else:
            t = table[lan][job][time][food]
            
            left = 0
            right = len(t)-1
            score = int(score)
            while left <= right:
                mid = (left + right) // 2
                if t[mid] < score:
                    left = mid + 1
                else:
                    right = mid - 1

            return len(t) - left

        return count


    for s in info:
        l = s.split()
        score = int(l.pop())
        lan, job, time, food = map(lambda x: d[x], l)
        table[lan][job][time][food].append(score)

    for i in range(3):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    table[i][j][k][l].sort()

    for q in query:
        lan, _, job, _ , time, _, food, score = q.split(" ")
        answer.append(f(lan,job,time,food,score,0))

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))