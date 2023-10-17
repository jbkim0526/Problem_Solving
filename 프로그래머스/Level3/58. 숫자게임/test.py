

a = [9,9,7,7,7,6,6,6,5,4,3,2]


left = -1
right = len(a)
num = 1

while left + 1 < right:
    mid = (left+right)//2
    if a[mid] <= num:
        right = mid
    else:
       left = mid




print(left,right)


