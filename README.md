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



# 다른언어와 다른 부분
<li> ** : 3 ** 4 는 3의 4승을 나타냄
<li> // : 나눗셈에서 소수부분을 버림
<li> """ : 따옴표 세개는 이스케이프 코드없이 개행도 해줌
<li> 문자열곱하기 : str * 2 는 strstr이 출력
<li> 문자열에서 음수 인덱스 : a[-1]은 문자열 끝에서부터 읽음
