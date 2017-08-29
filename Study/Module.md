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

<li> 모듈과 클래스

```python

```