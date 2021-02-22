### 학습에 참고한 사이트와 간단한 내용 
* https://wikidocs.net/32#ord : 파이썬 내장함수
* https://blockdmask.tistory.com/416 : 파이썬 대문자 소문자 변경 함수
* https://ooyoung.tistory.com/75 : 파이썬 최소, 최대값을 찾는 함수 dict min, max
* https://bio-info.tistory.com/40 : 파이썬 dictionary max value에 대한 key 찾기
* https://securityspecialist.tistory.com/73 : 파이썬 pass 와 continue 차이
* https://ooyoung.tistory.com/78 : find, index() 비교

### 오늘 발견한 문제 
1. Dic value 값들중 max, min으로 왜 해결할 수 없는가
2. Continue 와 pass의 차이점

### 해결 방안 
1. Max(dict)를 하면 딕셔너리의 키값중 최댓값이 출력됩니다. 하지만 키값중 최댓값을 찾는게 아닌 딕셔너리의 밸류값이 최댓값을 찾는데 그에 해당하는 키값을 출력하고 싶을때는 max(dict)를 이용하는게 아니라 max의 key로 value의 최댓값을 기준으로 잡아줘야 했습니다.
```
max(dict ,key=dict.get) # dict.get 이용 get은 해당value를 얻고싶을때 쓰는함수
```

2. pass의 기본 개념은 참과 거짓을 정의할때 아무런 일도 하지 않게 하는 것이고
continue는 반복문을 종료시키지 않고 맨처음의 조건문으로 넘어가는 것입니다.
```
>>> i = 0
>>> while i < 20 :
            i = i + 1
            if i % 3 == 0:    # 3의 배수 이면
                    continue    # 나머지가 0이면 while i < 20 으로 올라갑니다.
            print(i)	# 1부터 20까지중 3의배수를 제외하고 출력

>>> i = 0
>>> while i < 20 :
            i += 1    # i += 1은 i = i + 1과 같습니다.
            if i % 3 == 0:
                    pass
            print(i) #1~20까지 모두 출력

```

### 학습 내용에 대한 개인적인 총평 
- 딕셔너리에서 최대 최소의 값들의 키를 알고 싶을때는 max의 키 인자를 key=function 처럼 활용하여 기준을 바꾸면 쉽게 원하는 값을 찾을 수 있었습니다. 또, 원하는 숫자를 아스키코드로 바꾸거나 그와 반대로 적용시킬 경우 c처럼 그냥 서식지정자만 바꿔주면 변환되서 출력 될 줄 알았지만 파이썬은 아스키코드와 숫자로 변환하는 함수를 따로 제공하고 있었습니다. 그래서 ord와 chr함수에 대해 다시 공부하게 되었습니다.

### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      기본수학 1
