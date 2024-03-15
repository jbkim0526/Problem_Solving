import sys 
input = sys.stdin.readline 
from collections import defaultdict
from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int,input().split()))
cards.sort()

M = int(input())
numbers = list(map(int,input().split()))

for num in numbers:
    right = bisect_right(cards, num)
    left = bisect_left(cards, num)
    print(right-left,end=" ")



