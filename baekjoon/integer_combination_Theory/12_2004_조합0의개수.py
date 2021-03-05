#2004
'''
문제
(n m)의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n, m (0<=m<=n<=2000000000,n != 0 )이 들어온다.
출력
첫째 줄에 (n m)
의 끝자리 0의 개수를 출력한다.

예제 입력 1 
25 12
예제 출력 1 
2'''

'''import sys   #시간 초과 2000000000과 같은 엄청큰수는 팩토리얼 계산시 엄청오래걸림
import math
input = sys.stdin.readline

ret = math.comb(*map(int, input().split()))

flag = 0
for i in str(ret):
    if flag == 1 and i == '0':
        count += 1
    elif flag == 0 and i == '0':
        flag = 1
        count = 1
    else:
        flag = 0
        count = 0

print(count)'''

import sys
input = sys.stdin.readline

def num_divide(num, x):  #숫자들이 몇번나뉘는지 세기(2나 5로)
    cnt = 0             #0이 생기는경우는 10(2 * 5)이 만들어지는 경우
    while num != 0:
        num //= x
        cnt += num
    return cnt

n, m = map(int, input().split())
#nCm = n! / (m! * (n - m)!)이므로 이에맞춰 2의개수와 5의개수를 구한뒤에 더 작은값이 0이 됨
divde_2 = num_divide(n, 2) - num_divide(m, 2) - num_divide(n - m, 2)
divde_5 = num_divide(n, 5) - num_divide(m, 5) - num_divide(n - m, 5)
print(min(divde_2, divde_5))