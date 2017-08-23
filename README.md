# 문자열

---
### 문자열 슬라이싱 
문자열에서 문자열을 추출하는 방법
a[0:4]에서 마지막 글자는 포함되지 않음, a[0:3]의 경우 'Lif'가출력됨
<li> 일반적인 사용방법

```python
a = 'Life is good'
print a[0:4]
# 값 : Life
```

<li> 뒷글자를 생략하는 경우

```python
print a[1:]
#값 : ife is good;
```

<li> 앞글자를 생략하는 경우

```python
print a[:10]
#Life is go
```

<li>양쪽글자를 생략하는 경우

```python
print a[:]
#Life is good
```

<li> 문자열 나누기

```python
first = a[0:4]
last = a[4:]
```

---
### 문자열 포메팅
C언어의 프린트문과 유사

```python
"i eat %d apple %s" % (3,"When Last Day");
```

---
### 문자열 관련 함수

<li> count() : 문자 개수 세기
<li> find('a') : 해당 문자의 첫 번째 인덱스를 가져옮(없는 경우 -1 반환)
<li> index('a'):  해당 문자의 첫 번째 인덱스를 가져옮(없는 경우 오류 발생)
<li> upper() : 소문자를 대문자로 바꿈
<li> lower() : 대문자를 소문자로 바꿈
<li> lstrip() : 왼쪽 공백 삭제
<li> rstrip() : 오른쪽 공백 삭제
<li> strip() : 양 쪽 공백 삭제
<li> replace('str1','str2') : str1을 str2로 변경
<li> split() : 문자열을 나눔

---
#리스트 자료형

배열과 동일함

```python
a = [];
b = [1,2,3]
c = ['life','is','good']
```

---
### 리스트의 인덱싱
 
 문자열 인덱싱과 도일함
 
 ---
### 리스트 연산자

<li> + : 리스트를 합침
<li> * : 리스트 반복하기

---
### 리스트의 수정, 변경과 삭제

<li> 리스트에서 하나의 값 수정

```python
a = [1,2,3]
a[2] = 4
```

<li> 리스트에서 연속된 범위의 값 수정하기

```python
a[1:2] = ['a','b','c']  
# a[1] = ['a','b','c'] 와는 다른 결과, 이 경우 배열안에 배열이 들어가게 됨
```

<li> 리스트 값 삭제

```python
a[1:3] = [] # 빈 배열을 이용해 값 삭제
```

<li> del 함수를 사용해 리스트 요소 삭제

```python
del a[1] # del a[1:3]처럼 슬라이싱 가능
```

---
### 리스트 관련 함수들

<li> append('ele') : 리스트에 요소 추가
<li> sort() : 리스트 정렬
<li> reverse() : 리스트 뒤집기
<li> index(idx) : idx라는 값이 있으면 위치값 리턴(없는 경우 오류 발생)
<li> insert(idx,ele) : idx의 위치에 ele를 삽입
<li> remove(x) : x라는 요소가 첫 번째로 나오는 부분을 찾아서 삭제
<li> pop()  : 리스트의 맨 마지막요소를 돌려주고 그 요소는 삭제하는 함수
<li> count(x) : x가 얼마나 들어가있늕디 찾음
<li> extend(arr) : arr을 더해 리스트를 확장

---
# 튜플 자료형

튜플은 리스트와 다음과 같은 차이점이 있음

<li> 리스트는 []로 둘러싸지만 튜플은 ()로 둘러쌈
<li> 리스트는 그 값의 생성,삭제수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

더하기, 곱하기, 인덱싱, 슬라이싱이 가능하지만, 생성,삭제,수정은 불가능

---
# 딕셔너리 자료형

<li> key : value로 이루어져있음.
<li> {} 중괄호로 만들어짐

---
### 딕셔너리 쌍 추가, 삭제하기

<li> 추가

```python
a = {1:'a'}
a[2] = 'b'
a['name'] = 'pey' 
a[3] = [1,2,3]
```

<li> 삭제

```python
del a[1]
```

<li> key를 사용해 Value 얻기

```python
grade['pey']
```

---
### 딕셔너리 관련 함수들

<li> keys() : key 리스트를 만듬. dict_keys라는 객체를 리턴(list(a.keys())를 통해 리스트로 변환)
<li> values() : value 리스트를 만듬. dict_values라는 객체를 리턴
<li> items() : key,value 쌍얻기, 튜플로 묶은 값을 dict_items 객체로 돌려줌.
<li> clear() : 쌍 모두 지우기
<li> get('name') : 키로 밸류 얻기 (없는 경우 None)을 리턴함
<li> get('foo','bar') : 키값이 없는 경우 디폴트 값을 가져옮.

---
# 집합 자료형
<li> set 키워드로 생
<li> 중복을 허용하지 않음
<li> 순서가 없음

### 집합 자료형 활용
<li> 교집합

```python
s1 & s2
s1.intersection(s2)
#s1 과 s2 모두에게 속한 부분만 리턴
```

<li> 합집합

```python
s1 | s2
s1.union(s2)
# s1과 s2의 중복된 요소를 삭제하고 합침
```

<li> 차집합

```python
s1 - s2
s1.difference(s2)
#s1 중 s2의 중복된 요소를 삭제하고 남은 s1 요소 리턴
```

<li>값 1개 추가하기

```python
s1 = set([1,2,3])
s1.add(4)
```

<li> 값 여러 개 추가하기

```python
s1.update([4,5,6])
```

<li> 특정값 제거하기

```python
s1.remove(2)
```

---
# 자료형의 참거짓

<li> 문자열 : ""(거짓), "Any Word"(참)
<li> 리스트 : [](거짓), [1,2,3](참)
<li> 튜플 : ()(거짓)
<li> 딕셔너리 : {}(거짓)
<li> 숫자 : 0(거짓), 0이 아닌 숫자(참)
<li> None : 거짓

# 제어문

### 조건문

```python
money = 1
if money :
    print("go")
else :
    print("don't go ")
```

---
### and, or, not
<li> a and b : 둘다 참일 때
<li> a or b : 둘중 하나가 참일 때
<li> not a : a가 거짓이면

### in, not in
<li> x in a : x가 a 안에 있으면 참, 없으면 거짓.
<li> x not in a : x가 a 안에 없으면 참, 있으면 거짓.

### pass
아무 실행도 안하려고 할때.

```python
if a in x :
    pass
```

### elif 

else if문의 역할을 함.

```python
if card :
    pass
elif money :
    pass
else :
    pass
```

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

<li> for 문 안에 if 문 넣기
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

# 함수

<li> 함수의 원형

def 함수명(매개 변수) : 
 수행할 문장
 return 결과값

<li> 입력값이 몇 개가 될지 모르는 경우
인자 앞에 * 을 붙인다.

```python
def sum_many(*args):
    sum = 0 
    for i in args:
        sum += i
    return sum
```

<li> 리턴 값이 두개 이상 인 경우

```python

def sum_and_mul(a,b):
    return a+b,a*b   # 반환 값은 (a+b,a*b)의 튜플로 생성됨
# 만약 두개를 따로 받고 싶다면

sum, mul = sum_and_mul(3,7) ##이 경우 sum에는 10이 mul에는 21이 들어감
```

<li> 입력 인수에 초깃값 미리 설정하기

```python
def say_myself(name,old,man=True) : #초기화 시키고 싶은 것은 뒤에 위치해야함
    print("이름 %s" % name)
    print("나이 %d" % old)
    if man :
        print("남자")
    else :
        print("여자")
```

<li> global 명령어를 이용해서 전역 변수로 선언 

```python
def vartest():
    global a
    a = a + 1

```

---
#사용자의 입력과 출력

<li> input의 사용

```python
a = input("숫자를 입력하세요")
```

<li> print

```python
print("life" "is" "too short") # lifeistoo short 큰따옴표로 둘러싸인 문자열은 + 연산과 동일
print("life","is","too short") # life is too short  띄어쓰기는 콤마연산으로 함
```

---
# 파일 읽고 쓰기

<li> 파일 생성하기

```python
f = open("새파일.txt",'w') #open(파일이름, 파일 열기 모드)
f.close()
```

<li> 파일을 쓰기 모드로 열어 출력값 적기

```python
# writedata.py

f = open("C:/Python/새파일.txt",'w')
for i in range(1,11):
    data = "%d 번쨰 줄입니다.\n" %i
    f.write(data)
f.close()
```

# 파일을 읽는 방법

<li> readline() 함수 이용하기

```python
# readline.py

f = open("C:/Python/새파일","w")
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()
```

<li> readlines() 함수를 이용

```python
f = open("C:/Python/새파일","w")
lines = f.readlines() #리스트로 반환
for line in lines :
    print(line)
f.close()
```

<li> read() 함수 이용하기

```python
f = open("C:/Python/새파일","w")
data = f.read() # 하나의 문자열로 반환
print(data)
f.close()
```

### 파일에 내용 추가

<li> 내용 추가하기

```python
# adddata.py
f = open("C:/Python/새파일","a")
for i in range(11,20):
    data = "%d번재 줄입니다\n" %i
    f.write(data)
f.close()

```

<li> with 문과 함꼐 사용ㅎ기

```python
with open("C:/Python/새파일","w") as f : # with 작업 내용 as 변수 : 
    f.write("Life is too short,you need python")    

```






---
# 다른언어와 다른 부분
<li> ** : 3 ** 4 는 3의 4승을 나타냄
<li> // : 나눗셈에서 소수부분을 버림
<li> """ : 따옴표 세개는 이스케이프 코드없이 개행도 해줌
<li> 문자열곱하기 : str * 2 는 strstr이 출력
<li> 문자열에서 음수 인덱스 : a[-1]은 문자열 끝에서부터 읽음
<li> 복사

```python
a = [1,2,3]
b = a
a[1] = 4 
#a와 b모두 [1,4,3]의 값을 가짐. 주소값이 복사되는 듯
```

슬라이싱을 이용해 값만 복사

```python
b = a[:]
# 값만 복사
```

Copy 모듈을 사용

```python
from copy import copy #Copy모듈 사용
b = copy(a)
```