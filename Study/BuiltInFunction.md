# 내장 함수

<li> abs(x) : 숫자의 절대 값 반환

```python
abs(3) # 3

abs(-3) # 3
```

<li> all([x,y,z]) : 반복가능한 자료형이면 True반환 

```python
all([1,2,3])# True

all([1,2,3,0]) # False
```

<li> any(x) : x중 하나라도 참이 있을 경우 True

```python
any([1,2,3,0]) #True

any([0,""]) #False
```

<li> chr(i) : 아스키 코드 값을 입력받아 해당 하는 문자 출력

```python
chr(97) # a
chr(48) # 0
```

<li> dir(x) : 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌.

```python
dir([1,2,3]) # ['append','count'....] 리스트 관련 함수
dir({'1' : 'a'}) #['clear','copy' ...] 딕셔너리 관련 함수
```

<li> divmod(a,b) : a를 b 로 나눈 몫과 나머지를 튜플행텨로 리턴

```python
divmod(7,3) # (2,1) 몫 2 나머지 1
```

<li> enumerate : 순차 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체 반환

```python
for i, name in enumerate(['body','foo','bar']):
    print(i,name) # 0 body, 1 foo,2 bar
```

<li> eval : 실행 가능한 문자열을 입력받아 실행한 결과값을 리턴하는 함수

```python
eval('1+2') # 3
eval("'hi'+'a'") # hia
eval('divmod(4,3)') # 1,1
```

<li> filter : 첫 번쨰 인수로 함수를 두 번째 인수로 순차 자료형을 받아 참인것 만 묶어서 걸러냄

```python
def positive(numberList):
    result = []
    for num in numberList :
        if num > 0:
            result.append(num)
    return result
    
print(positive([1,-3,2,0,-5,6])) # 1,2,6

#filter 사용시

def positive(x):
    return x > 0
    
list(filter(positive,[1,-3,2,-5,0,6])) # 1,2,6 
```

<li> id : 객체를 입력받아 주소값 리턴

```python
a = 3
id(3) # 135072304
id(a) # 135072304
b=a
id(b) # 135072304
```

<li> input : 사용자 입력을 받는 함수

```python
a = input()
```

<li> int(x,y) : 문자열 형태의 숫자나 소수점이 있는 숫자를 y진수 정수형태로 리턴

```python
int('3')   # 3
int(3.4) # 3
```

<li> isinstance : 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.

```python
class Person : pass

a = Person()
isinstance(a,Person) #True
```

<li> len(s) : 입력값의 길이를 리턴

```python
len('python') #6 
len([1,2,3])  #3 
```

<li> list(s) : 반복 가능한 자료형을 리스트로 만들어 리턴하는 함수

```python
list("python") #['p','y','t','h','o','n']
list((1,2,3))  #[1,2,3]
```

<li> map(f,interable) : 반복가능한 자료형을 함수에 실행시켜 실행된 값을 묶어서 리턴하는 함수

```python
def two_times(x) :  return x*2
map(two_times,[1,2,3,4]) # 2,4,6,8
```

<li> max(x) : 순차 자료형을 입력받아 최대값 리턴
<li> min(x) : 최소값을 리턴

```python
a = [1,2,3]
max(a) # 3
min(a) # 1
```

<li> oct : 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴

<li> open : 파일 이름과 읽기 방법을 입력받아 파일 객체를 리턴

<li> ord : 문자의 아스키값을 리턴

<li> pow : x의 y제곱을 리턴하는 함수

```python
pow(2,4) # 16
pow(3,3) # 27
```

<li> range() : 입력바은 숫자를 반복가능한 객체로 만들어 리턴 

```python
# 인수가 하나인 경우 : 0 부터 시작함
list(range(5)) # 0~5

# 인수가 두개인 경우 
list(range(5,10)) # 5~10

#인수가 세개인 경우 : 마지막 인수는 숫자 사이의 거리
list(range(1,10,2)) # 1,3,5,7,9
```

<li> sorted(x) : 정렬하는 함수

```python
sorted([3,1,2]) # [1,2,3]
# 리스트의 sort 함수는 리스트 객체 내에 만 정리하고 반환은 하지 않음
```

<li> str(x) : 문자열 형태로 객체를 변환함

```python
str(3) # '3'
str('hi')  # 'hi'
```

<li> tuple(x) : 튜플로 만들어 반환
<li> type(x) : 입력값의 자료형이 무엇인지 알려줌
<li> zip(x) : 동일한 개수로 이루어진 자료형을 묶어주는 함수

```python
list(zip([1,2,3],[4,5,6])) # [(1,4),(2,5),(3,6)]
```
