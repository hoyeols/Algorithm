#10217 KCM Travel 다익스트라 다이나믹프로그래밍
'''문제
각고의 노력 끝에 찬민이는 2014 Google Code Jam World Finals에 진출하게 되었다. 구글에서 온 초대장을 받고 기뻐했던 것도 잠시, 찬찬히 읽어보던 찬민이는 중요한 사실을 알아차렸다. 최근의 대세에 힘입어 구글 역시 대기업답게 비용 감축에 열을 내고 있었던 것이다.
초대장 내용에 의하면 구글은 찬민에게 최대 M원까지의 비용만을 여행비로써 부담해주겠다고 한다. 인천에서 LA행 직항 한 번 끊어주는게 그렇게 힘드냐고 따지고도 싶었지만, 다가올 결승 대회를 생각하면 대회 외적인 곳에 마음을 쓰고 싶지 않은 것 또한 사실이었다. 그래서 찬민은 인천에서 LA까지 M원 이하로 사용하면서 도착할 수 있는 가장 빠른 길을 차선책으로 택하기로 하였다.
각 공항들간 티켓가격과 이동시간이 주어질 때, 찬민이 인천에서 LA로 갈 수 있는 가장 빠른 길을 찾아 찬민의 대회 참가를 도와주자.

입력
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 줄에는 공항의 수 N (2 ≤ N ≤ 100), 총 지원비용 M (0 ≤ M ≤ 10,000), 티켓정보의 수 K (0 ≤ K ≤ 10,000)가 공백으로 구분되어 주어진다. 이어서 K개의 줄에 걸쳐 각 티켓의 출발공항 u, 도착공항 v (1 ≤ u, v ≤ N, u ≠ v), 비용 c (1 ≤ c ≤ M, 정수), 그리고 소요시간 d (1 ≤ d ≤ 1,000) 가 공백으로 구분되어 주어진다. 인천은 언제나 1번 도시이고, LA는 언제나 N번 도시이다
출력
각 테스트 케이스당 한 줄에 찬민이 LA에 도착하는 데 걸리는 가장 짧은 소요시간을 출력한다.
만약, LA에 도착할 수 없는 경우 "Poor KCM"을 출력한다.

예제 입력 1
2
3 100 3
1 2 1 1
2 3 1 1
1 3 3 30
4 10 4
1 2 5 3
2 3 5 4
3 4 1 5
1 3 10 6
예제 출력 1
2
Poor KCM'''
import heapq
import sys
input = sys.stdin.readline
INF = (1e9)

def dijkstra(airport, clock, N, M):
	q = []
	heapq.heappush(q, (1, 0, 0))	#현재지점, 비용, 소요시간
	clock[1][0] = 0	#비용까지 고려

	for cost in range(M + 1):	#비용
		for here in range(1, N + 1):	#현재공항
			if clock[here][cost] == INF:
				continue
			distance = clock[here][cost]
			for next_here, next_cost, next_time in airport[here]:
				if cost + next_cost > M:
					continue
				clock[next_here][cost + next_cost] = min(clock[next_here][cost + next_cost], distance + next_time)
	return clock

def main():
	T = int(input())

	for _ in range(T):
		N, M, K = map(int, input().split())	#N = 공항의수, M = 총지원비용, K = 티켓정보의수
		airport = [[] for _ in range(N + 1)]	#공항이 그래프
		clock = [[INF for _ in range(M + 1)] for _ in range(N + 1)]		#시간이 거리행렬인데 한정점마다 비용까지 고려해야하므로 이중리스트로 표현
		for _ in range(K):
			u, v, c, d = map(int, input().split())	#u = 출발공항, v = 도착공항, c = 비용, d = 소요시간
			airport[u].append((v, c, d))	#그래프는 방향 그래프

		LA_clock = dijkstra(airport, clock, N, M)
		if min(LA_clock[N]) == INF:
			print("Poor KCM")
		else:
			print(min(LA_clock[N]))

if __name__ == "__main__":
	main()
