import math
numbers = list(float(n) for n in input().split())

num_width = math.ceil(numbers[0] / numbers[2])
num_height = math.ceil(numbers[1] / numbers[2])
print(num_width * num_height)
