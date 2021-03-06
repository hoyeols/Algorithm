#11050
'''문제
자연수 N과 정수 K가 주어졌을 때 이항계수 (N K)
를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
출력
(N K) 
를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10'''

#방법 1
import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
N_list = [i for i in range(N)]

print(len(list(combinations(N_list, K))))

#방법 2
'''import math
import sys
input = sys.stdin.readline

print(math.comb(*map(int, input().split())))    #object를 unpacking할때 *을 사용'''

#방법 3
'''import math
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ret = factorial(N) // (factorial(K) * factorial(N - K))
print(ret)'''
