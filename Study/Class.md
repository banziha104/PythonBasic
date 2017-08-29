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

<li> 클래스 상속

```python
class HouseKim(HousePark): #class 상속받을 클래스명(상속할 클래스명)
    lastname = "김"
```

<li> 메소드 오버라이딩

```python
class HouseKim(Housepark):
    lastname = "김"
    def travel(selfs,where,day): # 상속받는 클래스에서 상속한 클래스의 메소드를 그대로 써주면됨
        print("%s,%s 여행 %d 일" %(self.fullname,where,day))
```

<li> 연산자 오버로딩 

```python
class HousePark :
    lastname = "박"
    def __init__(self,name):
        self.funllname = self.funllname + name
    def __add__(self, other): #HousePark1 + HousePark2 시 호출
        print("합침")
    def __sub__(self, other): #HousePark1 - HousePark2 시 호출
        print("빼기")
        
    
```
