#14725_개미굴 알고리즘:트라이
'''문제
개미는(뚠뚠) 오늘도(뚠뚠) 열심히(뚠뚠)  일을 하네.
개미는 아무말도 하지 않지만 땀을 뻘뻘 흘리면서 매일 매일을 살길 위해서 열심히 일을 하네.
한 치 앞도(뚠뚠) 모르는(뚠뚠) 험한 이 세상(뚠뚠) 그렇지만(뚠뚠) 오늘도 행복한 개미들!
우리의 천재 공학자 윤수는 이 개미들이 왜 행복한지 궁금해졌다.
행복의 비결이 개미가 사는 개미굴에 있다고 생각한 윤수는 개미굴의 구조를 알아보기 위해 로봇 개미를 만들었다.
로봇 개미는 센서가 있어 개미굴의 각 층에 먹이가 있는 방을 따라 내려가다 더 이상 내려갈 수 없으면 그 자리에서 움직이지 않고 신호를 보낸다.
이 신호로 로봇 개미는 개미굴 각 층을 따라 내려오면서 알게 된 각 방에 저장된 먹이 정보를 윤수한테 알려줄 수 있다.
로봇 개미 개발을 완료한 윤수는 개미굴 탐사를 앞두고 로봇 개미를 테스트 해보기 위해 위 그림의 개미굴에 로봇 개미를 투입했다. (로봇 개미의 수는 각 개미굴의 저장소를 모두 확인할 수 있을 만큼 넣는다.)
다음은 로봇 개미들이 윤수에게 보내준 정보다.
KIWI BANANA
KIWI APPLE
APPLE APPLE
APPLE BANANA KIWI
(공백을 기준으로 왼쪽부터 순서대로 로봇 개미가 각 층마다 지나온 방에 있는 먹이 이름을 뜻한다.)
윤수는 로봇 개미들이 보내준 정보를 바탕으로 다음과 같이 개미굴의 구조를 손으로 그려봤다.
APPLE
--APPLE
--BANANA
----KIWI
KIWI
--APPLE
--BANANA
(개미굴의 각 층은 "--" 로 구분을 하였다.
또 같은 층에 여러 개의 방이 있을 때에는 사전 순서가 앞서는 먹이 정보가 먼저 나온다.)
우리의 천재 공학자 윤수는 복잡한 개미굴들을 일일이 손으로 그리기 힘들어 우리에게 그려달라고 부탁했다.
한치 앞도 모르는 험한 이세상 그렇지만 오늘도 행복한 개미들!
행복의 비결을 알기 위해 윤수를 도와 개미굴이 어떤 구조인지 확인해보자.

입력
첫 번째 줄은 로봇 개미가 각 층을 따라 내려오면서 알게 된 먹이의 정보 개수 N개가 주어진다.  (1 ≤ N ≤ 1000)
두 번째 줄부터 N+1 번째 줄까지, 각 줄의 시작은 로봇 개미 한마리가 보내준 먹이 정보 개수 K가 주어진다. (1 ≤ K ≤ 15)
다음 K개의 입력은 로봇 개미가 왼쪽부터 순서대로 각 층마다 지나온 방에 있는 먹이 정보이며 먹이 이름 길이 t는 (1 ≤ t ≤ 15) 이다.
출력
개미굴의 시각화된 구조를 출력하여라.
개미굴의 각 층을 "--" 로 구분하며, 같은 층에 여러개의 방이 있을 때에는 사전 순서가 앞서는 먹이 정보가 먼저 나온다.

예제 입력 1
3
2 B A
4 A B C D
2 A C
예제 출력 1
A
--B
----C
------D
--C
B
--A
예제 입력 2
4
2 KIWI BANANA
2 KIWI APPLE
2 APPLE APPLE
3 APPLE BANANA KIWI
예제 출력 2
APPLE
--APPLE
--BANANA
----KIWI
KIWI
--APPLE
--BANANA'''

import sys
input = sys.stdin.readline

class Node:
	def __init__(self, key):
		self.key = key
		self.child = dict()

class Trie:
	def __init__(self):
		self.head = Node(None)

	def insert(self, words):
		cur = self.head

		for c in words:
			if c not in cur.child:
				cur.child[c] = Node(c)
			cur = cur.child[c]
		cur.child['0'] = True

def print_trie(parents, stair):
	if '0' in parents.child:
		return
	sorted_trie = sorted(parents.child)
	for c in sorted_trie:
		print('--' * stair, end='')
		print(c)
		print_trie(parents.child[c], stair + 1)

trie = Trie()

N = int(input())
for _ in range(N):
	foods = input().split()

	K = int(foods.pop(0))
	trie.insert(foods)

root = trie.head
print_trie(root, 0)

'''
#trie를 안쓴 다른풀이
import sys
input = sys.stdin.readline

ant = []
N = int(input())
for _ in range(N):
	foods = input().split()
	K = int(foods.pop(0))
	ant.append(foods)

ant.sort()
for i in range(N):	#[['a', 'b', 'c', 'd'], ['a', 'c'], ['b', 'a']]
	if i == 0:
		for j in range(len(ant[i])):
			print('--' * j + ant[i][j])
	else:
		count = -1
		for j in range(len(ant[i])):
			if len(ant[i - 1]) <= j or ant[i - 1][j] != ant[i][j]: #전거보다 깊이가 깊거나 전거와 루트가 같이 않다면 멈추고 처음부터 출력
				break
			else:	#아니라면 j 부터 출력
				count = j
		for j in range(count + 1, len(ant[i])):
			print('--' * j + ant[i][j])
'''
