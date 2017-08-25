# 딕셔너리 자료형

<li> key : value로 이루어져있음.
<li> {} 중괄호로 만들어짐

---
### 딕셔너리 쌍 추가, 삭제하기

<li> 추가

```python
a = {1:'a'}
a[2] = 'b'
a['name'] = 'pey' 
a[3] = [1,2,3]
```

<li> 삭제

```python
del a[1]
```

<li> key를 사용해 Value 얻기

```python
grade['pey']
```

---
### 딕셔너리 관련 함수들

<li> keys() : key 리스트를 만듬. dict_keys라는 객체를 리턴(list(a.keys())를 통해 리스트로 변환)
<li> values() : value 리스트를 만듬. dict_values라는 객체를 리턴
<li> items() : key,value 쌍얻기, 튜플로 묶은 값을 dict_items 객체로 돌려줌.
<li> clear() : 쌍 모두 지우기
<li> get('name') : 키로 밸류 얻기 (없는 경우 None)을 리턴함
<li> get('foo','bar') : 키값이 없는 경우 디폴트 값을 가져옮.
