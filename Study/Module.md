# 모듈

<li> 모듈 불러오기

```python
# 저장한 위치로 이동한 다음 
import mod1

print(mod1,sum(3,4))
```

<li> 모듈 함수를 사용하는 다른 방법

```python
from mod1 import safe_sum
# from mod1 import sum,safe_sum
# from mod1 import *
safe_sum(3,4)
```

<li> if __name__ = "__main__" :

```python
#mod1.py
if __name__ == "__main__" :
    print("!")
    
# main.py
import mod1 # print문이 실행되지 않음
    
```

<li> 클래스를 포함한 모듈만들기

```python
#mod2.py

PI = 3.141592


class MyMath:

    def solve(self, r):
        return PI*(r**2)


def sum(a, b):
    return a+b

if __name__ == "__main__":
    print(PI)
    a = MyMath()
    print(a.solve(2))
    print(sum(PI , 4.4))
```
<li> 클래스를 포함한 모듈을 사용하기

```python
print(mod2.PI)
a = mod2.MyMath()
```
