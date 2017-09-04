# 외장 함수

---
### Sys 

파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈이다

<li> sys.argv : 명령 행에서 인수전달하기
<li> sys.exit() : 강제로 스크립트 종료하기
<li> sys.path : 파이썬 모듈들이 저장되어 있는 위치를 나타냄

```python
import sys
sys.path #['',파이썬 주소]  ''은 현재 디렉터리
```

---
### pickle 

객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

<li> dump : 파일에 저장함

```python
import pickle
f = open("text.txt",'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data,f) # dump함수를 이용하면 객체를 그대로 파일에 저장
```

<li> load : 불러오기

```python
import pickle
f = open("text.txt",'wb')
data = pickle.load(f)
```

---
### shuitl

파일을 복사해 주는 파이썬 모듈

```python
import shutil
shutil.copy("src.txt","dst.txt") #src라는 이름의 파일을 dst로 복사한다.
```

---
### glob

디렉터리에 있는 파일 이름을 모두 알아야할때 사용

```python
glob.glob("C:/Python/q*")
```

### time 

시간과 관련된 모듈

<li> time.time : UTC를 이용하여 현재시간을 실수형태로 리턴함
<li> time.localtime : 실수값을 이용해서 연도,월일시분초의 형태로바꿔줌

```python
import time
time.localtime(time.time()) # tm_year = 2017, tm_year = 8 ...
```

<li> time.asctime : time.localtime 의 반환된 튜플형태의 값을 알아보기 쉬운 형태로 리턴

```python
import time
time.asctime(time.localtime(time.time())) # Sat Apr 28 20:50:20
```

<li> time.ctime :  asctime 과 비슷하지만 현재 시간만을 리턴함

<li> time.strtime : 함수에 시간에 관계된 것을 세밀하게 표현할 수 있는 여러가지 포맷 코드를 제공(따로 봐야됨)

<li> time.sleep(x) : x초 만큼 쉼

---
### Calendar 

달력을 볼 수 있게 해주는 모듈

<li> calendar.calendar(연도 : 그 해의 전체 달력을 보여줌
<li> calender.weekday(연도,월,일) : 그 날짜에 해당하는 요일 정보를 리턴
<li> calender.monthrange(연도,월) : 입력받은 달의 1일이 무슨 요일인지와 그달이 며칠까지 있는지를 리턴

---
### Random 

난수를 발생시킴

<li> random.random() : 0.0과 1.0 사이에 실수 중에 난수값을 리턴
<li> random.randint(1,10) : 1과 10사이에 정수형 난수를 리턴
<li> random.choice(list) : list에서 무작위로 하나를 선택하여 리턴
<li> random.shuffle(list) : list를 무작위로 섞음

---

```python
aaaa
```