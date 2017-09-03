# 반복문

### while 문

```python
while True:
    if a :
        break
    else:
        print('not a')
```

### for 문

<li> 전형적인 for 문

```python
test_list = ['one','two','three']
for i in test_list:
    print(i)
```

<li> 이차원배열 for문

```python
a = [(1,2),(3,4),(5,6)]
for (first, last) in a :
    print(first, last)
```

<li> continue를 사용한 for문

```python
marks = [90,25,67,45,80]
number = 0
for mark in marks :
    number += 1
    if mark < 60 : continue # 60미만의 요소는 다음 문장이 실행되지 않고 넘어감.
    print("%d번 합격" % number)
```

<li> for문과 함께 사용뙤는 range 함수

```python
sum = 0
for i in range(1,11): # range 함수의 마지막은 세지않음. 1부터 10까지 더한값 출력 
    sum += 1 
print(sum)
```

<li> range함수를 이용한 구구단 예제

```python
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end= " ") # end = " "은 다음줄로 바로 넘어가지 않고 그 줄에서 계속 출력하기 위함 
    print('') # 개행, \n은 한줄 넘기고 뛰고 print('')은 바로씀 
```

<li>  리스트 안에 for 문 포함하기

```python
a = [1,2,3,4]
result = []
for num in a :
    result.append(num * 3)
```

<li> 리스트 내포
원형 : 표현식 for 항목 in 반복 가능 객체 if 조건 

```python
a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0]
print(result)
```

<li> for문을 리스트 안에 포함하기

```python
result = [x*y for x in range(2,10)
                for y in range(1,10)]
print(result)
```
