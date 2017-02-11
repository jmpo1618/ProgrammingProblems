e12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
colors = {0 : "black",
          1 : "brown",
          2 : "red",
          3 : "orange",
          4 : "yellow",
          5 : "green",
          6 : "blue",
          7 : "violet",
          8 : "gray",
          9 : "white"}

for _ in range(int(input())):
    inp = int(input())
    inp_str = str(inp)
    if inp >= 82000000000:
        print('gray', 'red', 'white')
        continue
    current = 0
    if len(inp_str) == 1:
        current = 10
    else:
        current = int(inp_str[:2])
    diff = abs(current - e12[0])
    closest = e12[0]
    for i in e12:
        if abs(current - i) <= diff:
            diff = abs(current - i)
            closest = i
    third = ""
    cur_str = inp_str
    closest_str = str(closest)
    if len(cur_str) < len(closest_str):
        third = "black"
    else:
        third = colors[abs(len(cur_str) - len(closest_str))]
    print(colors[int(closest_str[0])], colors[int(closest_str[1])], third)
