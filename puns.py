no = set(["pin", "pins", "pinned", "pinning", "pinner", "pinners"])

for _ in range(int(input())):
    count = 0
    for word in input().split():
        if "pin" in word.lower() and word.lower() not in no:
            count += 1
    print(count)
