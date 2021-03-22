# DFS & BFS
##### 학습에 참고한 사이트와 간단한 내용 
* https://itholic.github.io/python-bfs-dfs/ : [python]으로 bfs, dfs 구현해보기
* https://m.blog.naver.com/wideeyed/221541104629 : [Python] list append()와 extend() 차이점
* https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-2667%EB%B2%88-%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0-%EC%B4%88%EC%BD%94%EB%8D%94 : [백준/Python] 2667번 단지번호 붙이기

## 오늘 발견한 문제 
1. List 원소를 추가할 때 append 와 extend의 차이점
2. dfs와 bfs의 활용차이

## 해결 방안 
1. append는 리스트 끝에 1개를 넣고 extend는 리스트 끝에 iterable의 모든 항목을 넣습니다
```
A = [a, b, c, d]
B = ‘abc’
A.append(B)	#[‘a’, ‘b’, ‘c’, ‘d’, ‘abc’]

A = [a, b, c, d]
B = ‘abc’
A.extend(B)	#[‘a’, ‘b’, ‘c’, ‘d’, ‘a’, ‘b’, ‘c’]
```
2. bfs(Breath First Search, 너비우선탐색)는 한 단계씩 나아가면서 해당 노드와 같은 레벨에 있는 노드들(즉, 형제 노드들)을 먼저 순회하는 방식입니다. 큐로구현합니다.
dfs(Depth First Search, 깊이 우선탐색)은 한 노드의 자식을 타고 끝까지 순회한 다음, 다시 돌아와서 다른 형제의 자식을 타고 내려가며 순회하는 방식입니다. 재귀나 스택으로 구현합니다.
- 시간복잡도 :   O(V + E)
- 장점 : dfs는 매우넓은 그래프 탐색에 효과적이고 bfs는 매우 깊거나 무한에 가까운 그래프에 효과적임
- 단점 : dfs는 목표노드가 없는 경로에 깊이 빠질 수 있고 bfs는 목표 노드로의 경로 길이가 모두 같다면 비효과적임
- 활용 : dfs는 위상정렬, 사이클탐지 bfs는 최단경로, 최소신장트리
```
def dfs(start, visited):
    visited += [start]
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        start = queue.pop(0)
        for i in range(len(graph[start])):
            if graph[start][i] == 1 and (i not in visited):
                visited += [i]
                queue += [i]
    return visited
```

#### 학습 내용에 대한 개인적인 총평 
- 좌표문제를 풀때는 dx, dy라는 리스트를 선언해주면 좀더 쉽게 접근할수 있었고 그래프를 리스트나 딕셔너리 둘다 구현할 수 있다는것에 놀랍습니다.
 딕셔너리에 set을 이용하면 중복문제도 처리해줘서 간편할것 같았습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      최단 경로
