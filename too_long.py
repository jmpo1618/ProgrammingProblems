t = int(input())
for i in range(t):
    word = input()
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
    print(word)
