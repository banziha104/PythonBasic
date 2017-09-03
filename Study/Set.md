
# 집합 자료형
<li> set 키워드로 생성
<li> 중복을 허용하지 않음
<li> 순서가 없음

### 집합 자료형 활용
<li> 교집합

```python
s1 & s2
s1.intersection(s2)
#s1 과 s2 모두에게 속한 부분만 리턴
```

<li> 합집합

```python
s1 | s2
s1.union(s2)
# s1과 s2의 중복된 요소를 삭제하고 합침
```

<li> 차집합

```python
s1 - s2
s1.difference(s2)
#s1 중 s2의 중복된 요소를 삭제하고 남은 s1 요소 리턴
```

<li>값 1개 추가하기

```python
s1 = set([1,2,3])
s1.add(4)
```

<li> 값 여러 개 추가하기

```python
s1.update([4,5,6])
```

<li> 특정값 제거하기

```python
s1.remove(2)
```

---
# 자료형의 참거짓

<li> 문자열 : ""(거짓), "Any Word"(참)
<li> 리스트 : [](거짓), [1,2,3](참)
<li> 튜플 : ()(거짓)
<li> 딕셔너리 : {}(거짓)
<li> 숫자 : 0(거짓), 0이 아닌 숫자(참)
<li> None : 거짓
