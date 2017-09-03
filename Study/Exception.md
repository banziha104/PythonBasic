# 예외 처리

<li> try , exception문 

```python
try:
    4/0
except ZeroDivisionError as e:
    print(e)
# except : 오류 종류와 상관없이 오류가 발생하기만하면 실행
```

<li> try, exception , else 문

```python
try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
```

<li> try finally

```python
f = open ('foo.txt','w')
try : 
    f = open('foo.txt','r')
finally: 
    f.close()
```

<li> 오류 발생시키기

```python
class Bird:
    def fly(self):
        raise NotImplementedError
```