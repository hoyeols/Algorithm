# ### 학습에 참고한 사이트와 간단한 내용 
* https://wikidocs.net/22803 : map, filter
* https://itholic.github.io/python-iterable-iterator/ : [python] iterable? Iterator?
* https://wikidocs.net/30 : 예외처리
* https://wikidocs.net/64 : 람다(lambda)
* https://dojang.io/mod/page/view.php?id=2300 : 문자열 서식 지정자와 포매팅 사용하기

### 오늘 발견한 문제 
1. map과 filter의 차이
2. iterable과 iterator의 차이

### 해결 방안 
1. map과 filter의 공통점은 기존배열은 건드리지 않으면서 요소들을 순회한 후 새로운 배열을 리턴한다는 것이고, 차이점은 map은 콜백함수가 적용된 새 요소, filter는 조건문을 만족한 요소들을 반환한다는 점입니다.

2. iterable한 객체라는건 단순히 iterator로 변환 가능한객체를 의미합니다. 즉 값을 한개씩 순차적으로 접근이 가능하도록 만들 수 있다는 뜻입니다. iterable객체는 평소에 자주 사용하는 list나 딕셔너리가 될 수 있습니다.
```
li = [1, 2, 3, 4, 5] #iterable한 객체

li_iter = iter(li)#iterator로 변환

next(li_iter)  # 1
next(li_iter)  # 2
next(li_iter)  # 3
next(li_iter)  # 4
next(li_iter)  # 5
next(li_iter)  # StopIteration
```

### 학습 내용에 대한 개인적인 총평 
- 파이썬의 리스트는 정말 강력하다는 것을 느낀 학습입니다. c언어로 작성시 무수히 많은 코드들이 단 한줄만에 작성되는것을 보면서 감탄을 하지 않을 수 없었습니다.

### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      def
