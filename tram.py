n = int(input())
result = 0
inside = 0;
for i in range(n):
    nums = [int(i) for i in input().split()]
    inside -= nums[0]
    inside += nums[1]
    if(inside > result): result = inside
print(result)
