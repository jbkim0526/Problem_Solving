def f(x):
    i = 0
    n = len(x)
    while not x[i].isdigit(): i += 1
    head = x[:i]
    numberi = i
    while i < n and x[i].isdigit(): i += 1
    number = int(x[numberi:i])
    newhead = ""
    for char in head:
        if char.isalpha(): newhead += char.lower()
        else: newhead += char
    return newhead, number

def solution(files):
    files.sort(key = f)
    return files


print(solution(["F-15", "img020.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))