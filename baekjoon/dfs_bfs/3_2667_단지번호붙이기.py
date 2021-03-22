#2667
'''문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
0110100     0110200
0110101     0110202
1110101     1110202
0000111     0000222
0100000     0300000
0111110     0333330
0111000     0333000
<그림 1>  ->  <그림 2>
입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9'''
'''import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
data = []
cnt = []
for _ in range(N):
    data.append(list(input().rstrip()))

def bfs(i, j):
    queue = [[i, j]]
    data[i][j] = '0'
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = b + dx[k]
            y = a + dy[k]
            if 0 <= x < N and 0 <= y < N and data[y][x] == '1':
                data[y][x] = '0'
                queue.append([y, x])
                count += 1
    cnt.append(count)

for i in range(N):
    for j in range(N):
        if data[i][j] == '1':
            bfs(i, j)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)'''

import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
data = []
cnt = []
N = int(input())
for _ in range(N):
    data.append(list(input().rstrip()))

def dfs(i, j):
    global count
    data[i][j] = '0'
    count += 1
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < N and 0 <= y < N and data[x][y] == '1':
            dfs(x, y)

for i in range(N):
    for j in range(N):
        if data[i][j] == '1':
            count = 0
            dfs(i, j)
            cnt.append(count)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)