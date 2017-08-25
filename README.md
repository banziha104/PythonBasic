# Python 기본

[문자열](https://github.com/banziha104/PythonBasic/blob/master/Study/String.md)
[리스트](https://github.com/banziha104/PythonBasic/blob/master/Study/List.md)
[딕셔너리](https://github.com/banziha104/PythonBasic/blob/master/Study/Dictionary.md)
[집합](https://github.com/banziha104/PythonBasic/blob/master/Study/Set.md)


# 제어문

---
[조건문](https://github.com/banziha104/PythonBasic/blob/master/Study/If.md)
[반복문](https://github.com/banziha104/PythonBasic/blob/master/Study/Loop.md)
[함수](https://github.com/banziha104/PythonBasic/blob/master/Study/Function.md)

#입출력

[입력과 출력](https://github.com/banziha104/PythonBasic/blob/master/Study/IO.md)
[파일 입출력](https://github.com/banziha104/PythonBasic/blob/master/Study/FileIO.md)

# 파이썬 핵심

[클래스](https://github.com/banziha104/PythonBasic/blob/master/Study/Class.md)
[a](https://github.com/banziha104/PythonBasic/blob/master/Study/List.md)
[a](https://github.com/banziha104/PythonBasic/blob/master/Study/List.md)
[a](https://github.com/banziha104/PythonBasic/blob/master/Study/List.md)
[a](https://github.com/banziha104/PythonBasic/blob/master/Study/List.md)








[클래스](www.naver.com).








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