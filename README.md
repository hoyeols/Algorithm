##### 학습에 참고한 사이트와 간단한 내용 
* https://jeongdowon.medium.com/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-backtracking-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-13492b18bfa1 : 알고리즘  Backtracking 이해하기

## 오늘 발견한 문제 
1. 백트랙킹이란 무엇인가

## 해결 방안 
1.  위키디피아 정의에 따르면 ‘조건만족문제’를 해결하기 위해 쓰이는 알고리즘이고 ’The Algorithm design manual’책에는 백트렉킹에 대해서 어떤 테크닉인데 ‘조합 알고리즘 문제’에 대해 모든 가능한해를 나열하는 것이라고 정의합니다. 즉, 모든 조합의 수를 살펴보되 조건을 만족할 때만 살펴봅니다.
```
def backtrack-dfs(A, k):
	if A == (a1, a2, a3, …,ak) is a solution, report it
	else
		k += 1
		computes Sk
		while Sk != 0
			ak = element in Sk
			Sk = Sk - ak
			backtrack-dfs(A, k)
```
백트래킹은 '가능한 모든 방법을 탐색한다' 는데 기본 아이디어가 있습니다. 대표적인 완전 탐색 방법으로는 DFS (Depth First Search, 깊이 우선 탐색) 이 있습니다. DFS 는 현재 지점에서 방문할 곳이 있으면 재귀 호출을 이용해서 계속 이동하며 무한히 깊은곳을 찾아야할때 효과적입니다. 하지만 DFS 는 모든곳을 방문하기 때문에 굳이 목표지점이 있지 않는 경로로 빠져서 비효율적인 결과를 초래할수도 있습니다 따라서 위에서 언급한 constrain satisfaction problems(csp)를 통해 비효율적인 경로를 차단하고 목표지점에 갈수있는 루트를 검사하는 방법입니다.

#### 학습 내용에 대한 개인적인 총평 
- 백트랙킹을 이제까지 문제에 부딪혔을때 실패지점으로 돌아가 다른 방향으로 순회하는것으로 알고 있었는데 요번 학습을 통해 백트랙킹에 대하여 자세히 알게 되었습니다.
파이썬에서는 itertools에 조합과 순열을 모두 라이브러리로 구현해 놔서 모든 조합문제를 쉽게 접근할 수 있었습니다. 위 함수를 이용하여 백트랙킹 문제를 해결한다면 시간도 줄고 가독성도 높게 올릴수 있을거 같았습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      동적계획법
