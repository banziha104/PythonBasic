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
