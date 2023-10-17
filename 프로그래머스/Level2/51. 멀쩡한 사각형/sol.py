def gcf(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(w,h):
    answer = w*h
    if w == h:
        answer -= w
    else:
        g = gcf(w,h)
        answer -= (w//g + h//g - 1)*g
    return answer

print(solution(12,8))