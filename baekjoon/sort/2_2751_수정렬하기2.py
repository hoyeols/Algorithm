#2751.py
'''문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
5
5
4
3
2
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
sorted_list = []
for i in range(N):
    sorted_list.append(int(input()))

'''
#sorted()와 sort() 사용해보기 1544ms
sorted_list.sort()  #sorted_list = sorted(sorted_list)'''

#합병정렬 7812ms
def merge(x):
    if len(x) > 1:
        mid = len(x) // 2
        left, right = x[:mid], x[mid:]
        merge(left)
        merge(right)

        left_i, right_i, i = 0, 0, 0
        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                x[i] = left[left_i]
                left_i += 1
            else:
                x[i] = right[right_i]
                right_i += 1
            i += 1
        if left_i != len(left):
            x[i:] = left[left_i:]
        else:
            x[i:] = right[right_i:]
#merge(sorted_list)

#퀵정렬 #시간초과
def quick(x, start, end):
    if end <= start:    #원소가 하나일경우 정렬 끝
        return x
 
    pivot = x[(start + end) // 2]   #피봇을 가운데로 피봇에따라 쪼개는 비용이달라지므로 선정중요!
    left = start
    right = end

    while left <= right:    #피봇보다 작은값은 왼쪽으로 큰값은 오른쪽으로 정렬
        while x[left] < pivot:  #피봇보다 왼쪽이 작으면 패스
            left += 1
        while x[right] > pivot: #피봇보다 오른쪽이 크면 패스
            right -= 1
        if left <= right: #left와 right가 교차하지 않았으면
            x[left], x[right] = x[right], x[left]
            left, right = left + 1, right - 1

    quick(x, start, left - 1) #피봇기준 왼쪽 정렬
    quick(x, left, end) #피봇기준 오른쪽 정렬

quick(sorted_list, 0, len(sorted_list) - 1)

for i in sorted_list:
    print(i)
