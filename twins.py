n = int(input())
l = [int(i) for i in input().split()]
l.sort(reverse=True)
total = sum(l)
sum = 0
coins = 0
for i in l:
    sum += i
    coins += 1
    total -= i
    if sum > total:
        print(coins)
        break
