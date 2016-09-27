import sys
from collections import deque


def answer(st):
    scnt = 0
    pcnt = 0
    for c in st:
        if c == "*":
            scnt += 1
        elif c == "+":
            if scnt > 0:
                sys.stdout.write("*" * scnt)
                scnt = 0
            pcnt += 1
        else:
            sys.stdout.write(c)
    sys.stdout.write("*" * scnt)
    sys.stdout.write("+" * pcnt)


answer("2*4*3+9*3+5")
