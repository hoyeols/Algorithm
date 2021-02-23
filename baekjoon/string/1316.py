#1316.py
'''문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력 1 
3
happy
new
year
예제 출력 1 
3
예제 입력 2 
4
aba
abab
abcabc
a
예제 출력 2 
1'''
import sys
input = sys.stdin.readline

N = int(input())

count = 0
for i in range(N):
    word = input().strip()
    if list(word) == sorted(word, key=word.find): 
        count += 1

print(count)

'''T = int(input())
cnt = T
for i in range(T):
	word = input()
	for j in range(1, len(word)):
		#앞 글자가 처음 등장하는 인덱스보다 뒷 글자가 처음 등장하는 인덱스가 더 작으면, 뒷 글자는 앞서 이미 등장한 글자가 됩니다.
		if word.find(word[j-1]) > word.find(word[j]):
			cnt -= 1
			break
print(cnt)
'''