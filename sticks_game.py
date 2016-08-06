names = ["Akshat", "Malvika"]
nums = [int(i) for i in input().split()]
n = nums[0]
m = nums[1]
intersections = n * m
winner = 0
while intersections > 0:
    intersections -= (m + n - 1)
    n -= 1
    m -= 1
    winner += 1
print(names[winner % 2])
