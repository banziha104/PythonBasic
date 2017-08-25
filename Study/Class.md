# 클래스

<li> 클래스 선언 class 명령어를 이용

```python
class MyClass :
    pass
```

<li> 인스턴스 객체 생성

```python
a = Myclass()
```

<li> 변수, 함수 선언 및 접근

```python
class Service :
    secret = "비밀" # 클래스 변수 선언
    def sum(self,a,b): # 클래스 함수 선언 
        result = a + b
        print(result)
        
pey = Service()     # 인스턴스 생성
print(pey.secret)   # 변수 접근 
pey.sum(1,1)        # 변수를 통한 함수 접근
```

<li> self : 호출한 인스턴스 객체를 가르킴
<li> __init__ : 생성자

```python
class Service :
    secret = "비밀"
    def __init__(self,name):
        self.name = name 
    def sum(self,a,b):
        result = a + b
        print(result)
```

