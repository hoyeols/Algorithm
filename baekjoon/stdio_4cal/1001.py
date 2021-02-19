import sys
input = sys.stdin.readline #input()과 같은 동작을 하지만 더 빠름 https://velog.io/@gouz7514/%ED%8C%8C%EC%9D%B4%EC%8D%AC-input-vs-sys.stdin.readline

a, b = map(int, input().split())
print(a - b)