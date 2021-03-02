#15650.py
'''문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
예제 출력 1 
1
2
3
예제 입력 2 
4 2
예제 출력 2 
1 2
1 3
1 4
2 3
2 4
3 4
예제 입력 3 
4 4
예제 출력 3 
1 2 3 4'''
import sys
input = sys.stdin.readline

'''N, M = map(int, input().split())
check = [0] * (N + 1)
result = [0] * M

def backtracking(index, n, m):
    if index == m:
        for i in result:
            print(i, end=' ')
        print()
        return

    for i in range(1, n + 1):
        if index >= 1 and result[index - 1] > i:    #만약 수열에 넣을 숫자가 수열에있는 숫자보다 작다면 넣지마라
            continue
        if check[i] == 1:
            continue
        result[index] = i
        check[i] = 1
        backtracking(index + 1, n, m)
        check[i] = 0
backtracking(0, N, M)'''

from itertools import combinations

N, M = map(int, input().split())
num = [str(i + 1) for i in range(N)]

for i in map(' '.join, combinations(num, M)):
    print(i)
