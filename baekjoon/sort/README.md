##### 학습에 참고한 사이트와 간단한 내용 
* http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html : 파이썬으로 정렬 알고리즘 구현하기
* https://wikidocs.net/16041 : 리스트 정렬
* https://www.daleseo.com/python-collections-counter/ : [파이썬] collections 모듈의 Counter 클래스 사용법

# 오늘 발견한 문제 
1. 파이썬 정렬 알고리즘
2. sorted() 와 sort()의 차이

## 해결 방안 
1.
<table>
  <thead>
    <tr>
      <th style="text-align: center">Name</th>
      <th style="text-align: center">Best</th>
      <th style="text-align: center">Worst</th>
      <th style="text-align: center">Stable</th>
      <th style="text-align: center">Memory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center">버블정렬</td>
      <td style="text-align: center">n</td>
      <td style="text-align: center">n^2</td>
      <td style="text-align: center">True</td>
      <td style="text-align: center">1</td>
    </tr>
    <tr>
      <td style="text-align: center">선택정렬</td>
      <td style="text-align: center">n^2</td>
      <td style="text-align: center">n^2</td>
      <td style="text-align: center">False</td>
      <td style="text-align: center">1</td>
    </tr>
    <tr>
      <td style="text-align: center">삽입정렬</td>
      <td style="text-align: center">n</td>
      <td style="text-align: center">n^2</td>
      <td style="text-align: center">True</td>
      <td style="text-align: center">1</td>
    </tr>
    <tr>
      <td style="text-align: center">셸정렬</td>
      <td style="text-align: center">nlog n</td>
      <td style="text-align: center">(best) nlog ^2 n</td>
      <td style="text-align: center">False</td>
      <td style="text-align: center">1</td>
    </tr>
    <tr>
      <td style="text-align: center">병합정렬</td>
      <td style="text-align: center">nlog n</td>
      <td style="text-align: center">nlog n</td>
      <td style="text-align: center">True</td>
      <td style="text-align: center">n</td>
    </tr>
    <tr>
      <td style="text-align: center">퀵정렬</td>
      <td style="text-align: center">nlog n</td>
      <td style="text-align: center">nlog n ~ n^2</td>
      <td style="text-align: center">False</td>
      <td style="text-align: center">log n ~ n</td>
    </tr>  
- 버블정렬: 이웃한 두 값을 비교하여 정렬합니다. 최댓값이 맨 오른쪽으로 옮겨지며, 데이터가 잘 정렬되어 있을경우에 O(n)으로 데이터의 정렬여부를 파악하기 위해 사용하면 좋습니다. 만약 역순으로 정렬되어있는경우에는 (n - 1) + (n - 2) +…+1 번의 비교가 이루어지므로 O(n^2)입니다.
```
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)

``` - 선택정렬 : 주어진 배열에서 최댓값을 찾아 맨 오른쪽값과 교체합니다. 이웃한 두 값을 비교하지 않으므로 버블정렬보다 빠르지만 언제나 O(n^2)입니다.
```
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)
``` - 삽입정렬 : 원소를 배열 사이에 끼워 넣는 과정을 반복하면서 정렬합니다. 시간복잡도는 버블정렬과 똑같지만 평균적으로 버블정렬과 선택정렬보다 빠릅니다. ``` def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val ``` - 셸정렬 : 삽입정렬의 단점을 보완하기 위해 만든것으로 주어진 간격만큼 떨어진 서브배열을 만들어 삽입정렬을 수행합니다. 만약 간격이라 3이라면 3개의 서브배열을 만들고 모든 서브배열에 삽입정렬이 끝나면 간격을 반으로 줄여 다시 반복합니다. 배열이 이미 정리되어 있다면 O(nlogs)이고 최악의 경우에는 O(n^2)이고 다른 간격을 정의한다해도 O(nlog^2n)이 최선입니다. ``` def gapInsertionSort(x, start, gap):
    for target in range(start+gap, len(x), gap):
        val = x[target]
        i = target
        while i > start:
            if x[i-gap] > val:
                x[i] = x[i-gap]
            else:
                break
            i -= gap
        x[i] = val

def shellSort(x):
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(x, start, gap)
        gap = gap // 2
 ``` - 병합정렬 : 두 부분으로 쪼개는 작업을 재귀적으로 반복한뒤 비교하고 써클이 끝나면 두개씩 정렬된 거를 병합해나가며 정렬합니다. 두부분으로 쪼개는데 O(log n)이고 데이터병합에 O(n)이므로 언제나 O(nlog n)이지만 단점은 ㄹ데이터 크기만한 메모리가 더 필요합니다. ```
def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:] ``` - 퀵정렬 : 피벗 원소를 정하여 피벗보다 작은 값은 앞쪽에 큰값은 뒤쪽에 정렬합니다. 즉 병합정렬은 데이터를 쪼갠뒤에 합치는 과정에서 정렬하지만 퀵정렬은 데이터를 쪼개면서 정렬합니다. 데이터를 절반씩 쪼갠다면 이진탐색이므로 O(log n)이고 n개의 피봇과 비교하므로 O(n log n)입니다. 만약 데이터가 이미 정렬되어 있고 맨끝 원소를 피벗으로 선정한다면 쪼개는 비용만 O(n)이므로 시간복잡도가 O(n^2)까지 올라가며 또한 재귀호출을 위해 추가 메모리가 필요합니다. ```
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)
 ``` 
2.  sort와 sorted는 모두 정렬을 제공하는 함수인데 sort는 본체를 정렬하고 sorted는 정렬된 결과를 반환한다는 차이점이 있습니다. 
```
#sort
>>> a = [1, 10, 5, 7, 6]
>>> a.sort()
>>> a
[1, 5, 6, 7, 10]
>>> a = [1, 10, 5, 7, 6]
>>> a.sort(reverse=True)
>>> a
[10, 7, 6, 5, 1]

#sorted
>>> x = [1 ,11, 2, 3]
>>> y = sorted(x)
>>> x
[1, 11, 2, 3]
>>> y
[1, 2, 3, 11]
>>> x = [1 ,11, 2, 3]
>>> y = reversed(x)
>>> x
[1, 11, 2, 3]
>>> y
<list_reverseiterator object at 0x1060c9fd0>
>>> list(y)
[3, 2, 11, 1]
```

#### 학습 내용에 대한 개인적인 총평 
- 정렬 알고리즘을 여러가지 방법으로 구현해보아도 파이썬 기본 라이브러리에서 제공하는 sort와 sorted 보다 시간과 메모리면에서 비효율적이었습니다. 정렬알고리즘이 필요할 경우가 있다면 파이썬에서 제공하는 함수를 사용하는것이 더 수월할 것 같습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      백트랙킹
