from collections import deque

n, k = map(int,input().split())
durability = deque(list(map(int,input().split())))


belts = deque([None]*(2*n))
# 로봇의 belts에서 위치(index)
robot_indexs = []

ans = 0

while k > durability.count(0):
    # 1. 벨트가 각 칸의 로봇과 회전 (모두 한번에 이동)
    belts.rotate(1)
    durability.rotate(1)
    for i in range(len(robot_indexs)):
        robot_indexs[i] = (robot_indexs[i] + 1) % (2*n)

    # 벨트가 회전한 후 내리는 위치에 있으면 제거
    if belts[n-1]:
        belts[n-1] = None
        robot_indexs.remove(n-1)

    # 2. 먼저 벨트에 올라간 로봇부터 이동
    for robot_index in robot_indexs:
        n_index = robot_index + 1
        # 로봇이 있거나 내구도 1미만 이면 못감
        if belts[n_index] or durability[n_index] < 1:
            continue

        durability[n_index] -= 1
        belts[n_index] = belts[robot_index]
        belts[robot_index] = None
        i = robot_indexs.index(robot_index)
        robot_indexs[i] = (robot_indexs[i]+1) % (2*n)

    if belts[n-1]:
        belts[n-1] = None
        robot_indexs.remove(n-1)

    # 3. 올리기
    if durability[0]:
        belts[0] = 1
        durability[0] -= 1
        robot_indexs.append(0)
    ans += 1

print(ans)