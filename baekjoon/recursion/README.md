##### 학습에 참고한 사이트와 간단한 내용 
* https://readytoearndon.tistory.com/11 : 별찍기 설명:FBTT
* https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9Chanoi-top-in-python : 하노이탑 이동 순서

## 오늘 발견한 문제 
1. 하노이탑 알고리즘
2. 재귀 패턴 구하기

## 해결 방안 
1.  n개의 원판을 세번째 막대로 옮길시 1단계: n - 1개 원판이 2번에 있어야합니다 2단계: 마지막원판이 3번에 있어야합니다. 3단계: 2번에 있던 n -1개 원판을 3번으로 옮깁니다. 위과정을 재귀를 이용해 반복합니다.
```
def hanoi(n, one, two, three):
    if n == 1:  
        print(one, three)
    else:
        hanoi(n - 1, one, three, two)   
        print(one, three)
        hanoi(n - 1, two, one, three)
```
2.  부분이 전체와 같은 패턴을 갖고 있는 구조를 프랙탈 구조라고 합니다. n=27일때는 n=9일때의 star를 이용하여 n=27일때의 패턴을 다시 그려냅니다. 그리고 핵심아이디어는 n=3 일때는 2번째줄 n=9일때는 4,5,6번 째줄 n=27일때는 10~18번째줄. 즉, 출력하는 줄의 가운데라인 줄은 그전의 패턴에 빈칸을 해당 줄수만큼 채워주는 것입니다.
```
for i in range(rep):
    star = print_stars(star) #재귀 줄단위로 갱신

for i in range(3 * len(N)): #핵심아이디어
        if i // len(N) == 1:
            matrix.append(N[I % len(N)] + " " * len(N) + N[i % len(N)])
```

### 학습 내용에 대한 개인적인 총평 
- 재귀의 별찍기나 하노이탑 이동순서는 옛날에 종종 풀었던 문제지만 지금 다시 풀어보려고하니 어떻게 구현해야할지 감이 안잡혔습니다. 재귀란 큰문제를 작은문제로 나눈 다는점을 고려하면 쉽게 구현할텐데 아직 감이 잘 잡히지 않았던것 같습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      브루트포스
