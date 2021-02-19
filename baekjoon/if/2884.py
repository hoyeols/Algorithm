#2884.py
import sys
input = sys.stdin.readline

H, M = map(int, input().split())

M = M - 45
if (M < 0):
    H -= 1
    if (H < 0):
        H = 24 - 1
    M = 60 + M
print("%d %d" % (H, M)) #1. print("{} {}".format(H, M)) 2. print(H, M, sep=' ')