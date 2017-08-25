
# 파일 읽고 쓰기

<li> 파일 생성하기

```python
f = open("새파일.txt",'w') #open(파일이름, 파일 열기 모드)
f.close()
```

<li> 파일을 쓰기 모드로 열어 출력값 적기

```python
# writedata.py

f = open("C:/Python/새파일.txt",'w')
for i in range(1,11):
    data = "%d 번쨰 줄입니다.\n" %i
    f.write(data)
f.close()
```

# 파일을 읽는 방법

<li> readline() 함수 이용하기

```python
# readline.py

f = open("C:/Python/새파일","w")
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()
```

<li> readlines() 함수를 이용

```python
f = open("C:/Python/새파일","w")
lines = f.readlines() #리스트로 반환
for line in lines :
    print(line)
f.close()
```

<li> read() 함수 이용하기

```python
f = open("C:/Python/새파일","w")
data = f.read() # 하나의 문자열로 반환
print(data)
f.close()
```

### 파일에 내용 추가

<li> 내용 추가하기

```python
# adddata.py
f = open("C:/Python/새파일","a")
for i in range(11,20):
    data = "%d번재 줄입니다\n" %i
    f.write(data)
f.close()

```

<li> with 문과 함꼐 사용하기

```python
with open("C:/Python/새파일","w") as f : # with 작업 내용 as 변수 : 
    f.write("Life is too short,you need python")    

```
