# 우선순위큐 (힙 활용하기)
##### 학습에 참고한 사이트와 간단한 내용 
* https://www.daleseo.com/python-priority-queue/ : 파이썬의 우선순위 큐(PriorityQueue) 사용법
* https://www.daleseo.com/python-heapq/ : [파이썬] heapq 모듈 사용법
* https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html#:
~:text=%EC%97%AC%EB%9F%AC%20%EA%B0%9C%EC%9D%98%20%EA%B0%92%EB%93%A4%20%EC
%A4%91%EC%97%90%EC%84%9C%20%EC%B5%9C%EB%8C%93%EA%B0%92,%EC%A0%95%EB%A0%AC%20%EC%83%81%E
D%83%9C)%20%EB%A5%BC%20%EC%9C%A0%EC%A7%80%ED%95%9C%EB%8B%A4.&text=%EA%B0%84%EB%8B%A8%ED%9E%88%20%EB%
A7%90%ED%95%98%EB%A9%B4%20%EB%B6%80%EB%AA%A8%20%EB%85%B8%EB%93%9C%EC%9D%98,%EC%9E%91%EC%9D%80)%20%EC
%9D%B4%EC%A7%84%20%ED%8A%B8%EB%A6%AC%EB%A5%BC%20%EB%A7%90%ED%95%9C%EB%8B%A4. : [자료구조] 힙(heap) 이란

## 오늘 발견한 문제 
1. 자료구조 힙과 우선순위큐란
2. 모듈에서 최대힙으로 활용하기

## 해결 방안 
1. 우선순위큐는 선입선출하는 큐와달리 추가는 어떤순서대로 해도 상관없지만 제거될때는 가장 작은 값을 제거하는 자료구조 입니다. 
데이터를 정렬된 상태로 보관하며 heapq 모듈을 통해 구현되어 있습니다. 우선순위큐는 배열, 연결릭스트, 힙으로 구현이 가능하지만 삽입과 삭제가 O(log n)으로 힙이 가장 구현하기 적합합니다.
- 시간복잡도 :   PriorityQueue 클래스의 put(), get() 함수는 O(log n)
- 장점 : 힙으로 구현시 삽입과 삭제가 빠르다
- 단점 : 배열과 연결리스트로 구현시 O(n)의 복잡도를 가질 수 있다
- 활용 : 시뮬레이션시스템, 네트워크트래픽제어, 운영체제에서의 작업스케줄링, 수치해석적인계산
```
from queue import PriorityQueue
# 큐 생성
que = PriorityQueue()
#큐에 원소추가
que.put(4)
que.put(3)
que.put(2)
que.put(1)

#우선순위 큐에서 원소삭제
print(que.get())  # 1 
print(que.get())  # 2
print(que.get())  # 3
print(que.get())  # 4

#정렬기준 변경
que.put((3, 3))
que.put((1, 1))
que.put((2, 2))

print(que.get()[1])  # 3
print(que.get()[1])  # 2
print(que.get()[1])  # 1

```
힙은 완전 이진트리의 일종으로 우선순위 큐를 위해 만들어진 자료구조입니다. 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조로 반정렬상태를 유지합니다. 
최소힙 기준으로 작은값이 부모에 위치하고 자식들은 부모보다 큰값이 와야합니다. 완전 이진트리에서는 중복값을 허용하지 않지만 힙트리는 중복값을 허용합니다.
```
Import heapq

Heap = []	#모듈의 함수를 호출할때마다 리스트를 인자로 넘겨야합니다.
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)	#[1,3,7,4]
print(heapq.heappop(heap))	#1 ->[3,4,7]
```
2. 힙 모듈은 최소힙 기능만 동작하기 때문에 최대힙을 구현하려면 각 값에 대한 우선순위를 튜플을 이용해 힙에 추가해야합니다.
```
for _ in range(N):
    x = int(input())
    if (x != 0):
        heapq.heappush(heap, (-x, x)) #(우선 순위, 값)의 튜플형태로 최대힙
    else:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap)[1])   #ex : (-2, 2)에서 [0]은 우선순위 [1]은 값이므로
```

#### 학습 내용에 대한 개인적인 총평 
- 옛날에 알고리즘 문제를 풀때 heapq를 종종 사용했었는데 어떤원리로 정렬되는지 모른채로 그냥 사용했었습니다. 
오늘 학습을 통해서 heap이 어떻게 추가 삭제되며 어떤원리로 구성되어있는지 알았더니 더 쉽게 코드를 작성할 수 있었습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      dfs와 bfs
