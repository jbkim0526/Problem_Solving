N =3

print(3 & 1)

for i in range(1<<N):
    print(i)
    for j in range(N):
        print("True" if i & (1<<j) else "False")
    