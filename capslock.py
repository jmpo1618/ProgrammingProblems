s = input()
if s.isupper():
    s = s.lower()
elif s[0].islower:
    if s[1:] and s[1:].isupper():
        s = s[0].upper() + s[1:].lower()
    elif not s[1:]:
        s = s.upper()
print(s)
