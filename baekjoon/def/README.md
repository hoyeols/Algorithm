### 학습에 참고한 사이트와 간단한 내용 
* https://devpouch.tistory.com/69#:~:text=%EC%9D%B8%EB%8D%B1%EC%8A%A4%EB%A1%9C%20%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0&text=del%20%ED%82%A4%EC%9B%8C%EB%93%9C%EB%A5%BC%20%ED%86%B5%ED%95%B4%20%EB%A6%AC%EC%8A%A4%ED%8A%B8,%EC%9C%84%EC%B9%98%ED%95%9C%20%EC%9A%94%EC%86%8C%EA%B0%80%20%EC%A7%80%EC%9B%8C%EC%A7%91%EB%8B%88%EB%8B%A4. : 파이썬 리스트 요소 제거하기
* https://pydole.tistory.com/entry/Python-%ED%8F%AC%ED%95%A8Containment-%EC%97%B0%EC%82%B0%EC%9E%90-in-not-in : [python] 포함 연산잔 in, not in

### 오늘 발견한 문제 
1. 브루트 포스 알고리즘이란
2. 해당 리스트에 포함된 내용 제거하기

### 해결 방안 
1. 완전탐색 알고리즘으로 가능한 모든 경우의 수를 모두 탐색하여 요구조건에 충족된 결과만을 가져옵니다. 선형 구조를 전체적으로 탐색하는 방법에는 순차탐색, 비선형 구조를 전체적으로 탐색하는 방법에는 dfs와 bfs가 있습니다.

2. 해당 리스트에 포함된 내용을 제거하고 싶어서 순차탐색하며 해당 값을 리스트.remove(값)을 이용하거나 리스트.pop(index) or del list[index] 방법을 제거하려고 했습니다. 하지만 포함연산자 In 과 not in 을 이용하면 더욱 편리할것 같아서 포함 연산자를 이용했습니다.
```
Producer = []
for num in range(1, 10001):
    if d(num) > 10000:
        pass
    producer.append(d(num))

self_num = [i for i in range(1, 10001) if i not in producer]
```

### 학습 내용에 대한 개인적인 총평 
- 요번 학습에서는 문제를 이해하는데 시간 소요가 너무 오래 걸렸습니다. 또한 등차수열의 개념을 까먹어 등차후열에 대해서도 다시 공부하느라 진도가 좀 뎌딘것 같았습니다.

### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      문자열
