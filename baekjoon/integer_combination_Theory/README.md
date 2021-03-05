##### 학습에 참고한 사이트와 간단한 내용 
* https://ko.wikipedia.org/wiki/%EC%9D%B4%ED%95%AD_%EA%B3%84%EC%88%98#:~:text=%EC%A1%B0%ED%95%A9%EB%A1%A0%EC%97%90%EC%84%9C%2C%20%EC%9D%B4%ED%95%AD%20%EA%B3%84%EC%88%98(%E4%BA%8C,%EC%97%86%EB%8A%94)%20%EC%A1%B0%ED%95%A9%EC%9D%98%20%EA%B0%80%EC%A7%93%EC%88%98%EC%9D%B4%EB%8B%A4. : 이항계수
*https://mingrammer.com/understanding-the-asterisk-of-python/ : 파이썬의 Asterisk(*) 이해하기

## 오늘 발견한 문제 
1. 조합론에서 이항계수란
2. 컨테이너 타입의 데이터를 unpacking 하는법

## 해결 방안 
1.  조합론에서 이항계수는 이항식을 이항 정리로 전개했을때 각 항의 계수이며, 주어진 크기의 조합의 가짓수입니다. 이항계수를 nCk로 쓰기도 합니다. 그래서 저는 math라이브러리의 팩토리얼이나 comb나 itertools의 combinations를 활용해 문제를 해결했습니다.
```
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
```
2. Map object를 바로 unpacking하여 바로 comb함수에 이용하려고할때 asterisk(*)을 사용하여 map object를 unpacking 하였습니다. 함수가 변수를 받고 있기 때문에 리스트의 데이터를 모두 unpacking하여 함수에 전달해야 했습니다. 이 경우 함수에 값을 전달할 때 *map와 같이 전달하면 map object의 모든 값들이 unpacking되어 각 변수로  저장됩니다. Ex: `print(math.comb(*map(int, input().split())))`

#### 학습 내용에 대한 개인적인 총평 
- n!에 2가 들어있는 개수를 세기 위해서는 2의 제곱수로 나눈 몫을 계속해서 더한 것이 2의 총 갯수가 되는것이었습니다. nCm = n!/ m! * (n-m)! 인것에 맞춰 2의 갯수와 5의 갯수를 구한것이 왜 0과 관련이 있는지는 알았지만 min값이 왜 뒤에서부터의 0의 개수인지는 아직 이해하지 못했습니다. 또 팩토리얼은 계산량이 너무 많아서 시간이 오래걸린다는것 또한 학습하였습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      스택
