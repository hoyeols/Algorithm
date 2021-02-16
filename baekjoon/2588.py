import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = b
while (b):
    print(a * (b % 10))
    b = b // 10
print(a * c)

'''
#다른방법 2
a = int(input())
b = int(input())
ret1 = a * ((b % 10)
ret2 = a * (b // 10 % 10)
ret3 = a * (b // 100)
ret4 = a * b
print(ret1, ret2, ret3, ret4, sep='\n')'''