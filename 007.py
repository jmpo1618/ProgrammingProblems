message = input()
n = int(input())

i = 0
result = ""
while i < len(message):
    if i + n > len(message) - 1:
        for c in reversed(range(i, len(message))):
            result += message[c]
    else:
        for c in reversed(range(i, i + n)):
            result += message[c]
    i += n
    if i < len(message):
        if i + n > len(message) - 1:
            result += message[i:len(message)]
        else:
            result += message[i: i + n]
        i += n
print(result[:len(message)])
