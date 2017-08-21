#문자열

### 문자열 슬라이싱 
문자열에서 문자열을 추출하는 방법
a[0:4]에서 마지막 글자는 포함되지 않음, a[0:3]의 경우 'Lif'가출력됨
<li> 일반적인 사용방법

```python
a = 'Life is good'
print a[0:4]
# 값 : Life
```

<li> 뒷글자를 생략하는 경우

```python
print a[1:]
#값 : ife is good;
```

<li> 앞글자를 생략하는 경우

```python
print a[:10]
#Life is go
```

<li>양쪽글자를 생략하는 경우

```python
print a[:]
#Life is good
```

<li> 문자열 나누기

```python
first = a[0:4]
last = a[4:]
```

### 문자열 포메팅
C언어의 프린트문과 유사

```python
"i eat %d apple %s" % (3,"When Last Day");
```

### 문자열 관련 함수

<li> count() : 문자 개수 세기
<li> find('a') : 해당 문자의 첫 번째 인덱스를 가져옮(없는 경우 -1 반환)
<li> index('a'):  해당 문자의 첫 번째 인덱스를 가져옮(없는 경우 오류 발생)
<li> upper() : 소문자를 대문자로 바꿈
<li> lower() : 대문자를 소문자로 바꿈
<li> lstrip() : 왼쪽 공백 삭제
<li> rstrip() : 오른쪽 공백 삭제
<li> strip() : 양 쪽 공백 삭제
<li> replace('str1','str2') : str1을 str2로 변경
<li> split() : 문자열을 나눔











# 다른언어와 다른 부분
<li> ** : 3 ** 4 는 3의 4승을 나타냄
<li> // : 나눗셈에서 소수부분을 버림
<li> """ : 따옴표 세개는 이스케이프 코드없이 개행도 해줌
<li> 문자열곱하기 : str * 2 는 strstr이 출력
<li> 문자열에서 음수 인덱스 : a[-1]은 문자열 끝에서부터 읽음
