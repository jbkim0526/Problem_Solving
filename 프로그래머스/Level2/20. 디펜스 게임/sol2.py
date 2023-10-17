from queue import PriorityQueue

def solution(n, k, enemy):
    answer = 0

    enemies = len(enemy)
    q = PriorityQueue(maxsize=enemies)
    enemies_sum = 0
    count = 0

    for i in range(enemies):
        enemy_num = enemy[i]
        q.put(-1*enemy[i])
        enemies_sum += enemy_num
        if enemies_sum > n:
            count += 1
            if count > k:
                break
            enemies_sum += q.get()
        answer += 1
    return answer

print(solution(7,	3	,[4, 2, 4, 5, 3, 3, 1]))