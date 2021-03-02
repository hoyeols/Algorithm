#15649.py
'''문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
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
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
예제 입력 3 
4 4
예제 출력 3 
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = [0] * (N + 1)
result = [0] * M

def backtracking(index, n, m):  #dfs원리
    if index == m:  #index 하나씩 증가시키다가 m과 같아지면 출력하고 함수종료
        for i in range(m):
            print(result[i], end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        if check[i] == 1:   #이전에 사용했으면 다음 반복문
            continue
        result[index] = i   #i는 계속증가하지만 index는 m만큼 고정
        check[i] = 1        #수열에 사용되었다면 체크
        backtracking(index + 1, n, m)
        check[i] = 0    #다음수 넘어가기전에 초기화하기
backtracking(0, N, M)

'''from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N + 1))

for i in list(map(' '.join, permutations(li, M))):
    print(i)'''