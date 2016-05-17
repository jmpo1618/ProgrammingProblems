nums = [int(i) for i in input().split()]
dollars = ((nums[2] * (nums[2] + 1)) // 2) * nums[0]
if nums[1] >= dollars: print("0")
else: print(dollars - nums[1])
