#2750.py
'''문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
5
5
2
3
4
1
예제 출력 1 
1
2
3
4
5'''
import sys
input = sys.stdin.readline

N = int(input())
num_lst = []
for i in range(N):
    num_lst.append(int(input()))

'''
#sorted()와 sort() 사용해보기 68ms
num_list.sort()  #num_list = sorted(num_list)'''

#버블정렬 168ms
def bubble(x):
    for size in range(len(x) - 1, 0, -1):
        for i in range(size):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
#bubble(num_lst)

#선택정렬 148ms
def selection(x):
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
#selection(num_lst)

#삽입정렬 140ms
def insertion(x):
    for i in range(1, len(x)):
        for j in range(i):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i] 
insertion(num_lst)

for i in num_lst:
    print(i)