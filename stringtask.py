st = input()
vowels = set(["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"])
result = ""
for char in st:
    if not char in vowels:
        result += "."
        if char.isupper():
            result += char.lower()
        else:
            result += char
print(result)
