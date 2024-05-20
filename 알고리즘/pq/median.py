from heapq import heappush, heappop

nums = [23,41,13,22,-3,24,-31,-11,-8,-7,3,5,110,211,-311,-45,-67,-73,-81,-99,-33,24,56]
N = len(nums)

# left: max heap, right: min heap
left,right,ans = [],[],nums[0]

for i in range(1,N):
	num = nums[i]
	if num < ans:
		heappush(left, -1*num)
	else:
		heappush(right, num)
		
	# 홀수개이면 left right 개수를 맞출 수 없다
	# 짝수개가 되면 left right 개수를 비교해서 맞춘다.
	# 가능한 경우의 수는 4개 LR, RL, LL, RR
	# 4개 중 조정이 필요한 경우는 LL, RR
	if i % 2 == 0:
		if len(left) > len(right):
			heappush(right, ans)
			ans = -1* heappop(left)
		elif len(right) > len(left):
			heappush(left,-1*ans)
			ans = heappop(right)
	
print(ans)
nums.sort()
print(nums)