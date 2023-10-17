def solution(clothes):
    answer = 1
    d = {}
    for name, cloth_type in clothes:
        if cloth_type not in d:
            d[cloth_type] = 1
        else:
            d[cloth_type] += 1
    print(d)
    for v in d.values():
        answer *= (v+1)
    answer -= 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))