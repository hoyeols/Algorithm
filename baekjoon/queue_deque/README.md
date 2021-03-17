# queue_deque
##### 학습에 참고한 사이트와 간단한 내용 
* https://mong9data.tistory.com/50 : [자료구조][파이썬/Python] 덱 (Deque)
* https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue : [자료구조]스택(Stack), 큐(Queue), 덱(Deque)
* https://blockdmask.tistory.com/410 : 파이썬 문자열 count함수에 대해서
* https://itholic.github.io/python-reverse-reversed/ : reverse, reversed 차이
* https://pacific-ocean.tistory.com/232 : [백준] 18258(python 파이썬)
* https://chancoding.tistory.com/41 : [Python] 백준 5430 AC 효율적인 알고리즘

## 오늘 발견한 문제 
1. 큐와 덱의 정의와 장단점 시간복잡도
2. reverse와 reversed 차이 
3. counter의 사용법과 count()함수와의 차이
4. 시간복잡도 개선하기

## 해결 방안 
1. 큐는 FIFO(First In First Out)의 구조로 먼저 넣은 데이터가 먼저 나옵니다. 큐는 기다리는 줄에서 먼저 선 사람이 먼저 나갈 수 있는 것처럼 , 먼저 들어간 데이터가 먼저 나가는 것에서 붙여진 이름입니다. 데이터가 삽입하는것을 push 삽입되는 곳을 front 제거하는것을 pop 제거되는곳을 back 이라고 합니다. 순환 큐(환형 큐)는 선형 큐를 보완하기 위한 방식으로  front가 큐의 끝에 닿으면 큐의 맨 앞으로 자료를 보내서 원형으로 연결하는것을 말합니다.
- 시간복잡도 : 원소를 삽입하는경우에는 O(1) 삭제하는경우에는 O(n)이 필요합니다. -장점 : 데이터의 삽입이 빠릅니다 O(1)
-단점 : queue의 중간에 위치한 데이터로의 접근이 어렵고 배열로 구현했을 때, 선형 큐에서Front는 고정, Back을 이동하면서 데이터를 삭제하는 경우 데이터를 제거했을 때, 나머지 데이터를 한 칸씩 다 옮겨야 합니다. 둘 다 이동하면서 삽입, 삭제를 할 경우 배열의 끝에 저장되어 있는 상황되면, Back을 더 이상 이동시킬 수 없어서 overflow 발생할 수 있습니다.
-활용 : 데이터를 입력된 순서대로 처리할때, BFS구현할때, 콜센터 대기순서, 프로세스관리

덱은 queue와 비슷하지만 queue는 front에서만 삭제하고 back에서 삽입하는데, deque는 front와 end에서 삭제와 삽입이 모두 가능합니다. 중간 요소가 삽입, 삭제될 때, 요소들을 앞/뒤로 밀 수 있으므로 vector보다는 좋은 성능을 갖습니다. 앞/뒤에서의 삽입/삭제 성능은 좋지만 중간에서는 좋지 않습니다.
- 시간복잡도 : 삽입/삭제 원소를 앞/뒤에 삽입/삭제 할 시 O(1) -장점 : 데이터의 삽입과 삭제가 빠르며 앞, 뒤에서 데이터를 삽입/삭제할 수 있습니다.
-단점 : 중간에서의 삽입과 삭제가 어렵고 구현이 어렵습니다
-활용 : 데이터 개수가 가변적이며 앞/뒤에서 삽입 삭제가 자주 일어날 경우, 랜덤요소 접근
2. 
```
#reverse
l = ['a', 'b', 'c']
l_reverse = l.reverse()

print(l_reverse)  # None
print(l)  # ['c', 'b', 'a']
#reversed
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')

list(reversed(l))  # ['c', 'b', 'a']

```
reverse()는 객체 원본을 바꿔주며 원본을 바꾸지 않고 reversed는 객체를 반환합니다.
3.
```
#count
a = ‘pythonpp’ 
# 문자열에서 ‘p’가 몇개 있는지 ? 
print(a.count(p)) #3

#Counter
from collections import Counter
Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```
string.count(self, x, __start, __end) 함수는 문자열에서 쓰이는 메서드로 특성 문자가 string에서 몇개있는지 반환하는 함수입니다. Counter는 collections에 있는 패키지로 각 문자가 딕셔너리 형태로 몇개있는지 반환하며 데이터의 개수가 많은 순으로 정렬되어 반환합니다.
4.
```
	elif (i[0] == "pop"):
        	if (not queue):
            		print(-1)
        	else:
            		print(queue.popleft())
```
파이썬 리스트 기본제공함수에 pop를 사용할때 del함수를 써주게 되면 나머지 요소들이 앞으로 땡겨지는데 시간이 걸리므로 deque를 사용하여 popleft()함수를 써줬습니다 

#### 학습 내용에 대한 개인적인 총평 
- 시간복잡도를 개선하기위해 전혀 다른방식으로 접근해야 하는것이 너무 어려웠습니다. 도저히 방도가 생

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      우선순위큐
