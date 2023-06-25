# 딕셔너리 / 집합

'''
1. 딕셔너리
  1-1. 딕셔너리 쌍 추가하기
  1-2. 딕셔너리 요소 삭제
  1-3. 사용
  1-4. 관련 함수
2. 튜플
  2-1. 생성
  2-2. 교집합/합집합/차집합
  2-3. 관련 함수
'''

# 1. 딕셔너리
print('1. 딕셔너리')
# 1-1. 딕셔너리 쌍 추가하기
print("1-1. 딕셔너리 쌍 추가하기")

a = {1: 'a'}
a[2] = 'b' # 추가
print(a) # result : {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a) # result : {1: 'a', 2: 'b', 'name': 'pey'}

a['3'] = [1,2,3]
print(a) # result : {1: 'a', 2: 'b', 'name': 'pey', 3: [1,2,3]}



# 1-2. 딕셔너리 요소 삭제
print("\n1-2. 딕셔너리 요소 삭제")

del a[1]
print(a) # result : {2: 'b', 'name': 'pey', 3: [1,2,3]}



# 1-3. 사용
print("\n1-3. 사용")
grade = {'pey': 10, 'julliet': 99}

# key의 값으로 value 반환
print(grade['pey']) # result : 10

print(grade['julliet']) # result : 99

a = {1: 'a', 2: 'b'}
print(a[1]) # result : a

print(a[2]) # result : b

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(dic['name']) # result : 'pey

print(dic['phone']) # result : 0119993323

print(dic['birth']) # result : 1118

# 주의사항 : 같은 키값을 사용하면 앞의 value가 무시되고 가장 뒤의 value만 반환받을 수 있다.
# 주의사항 : 리스트를 키값으로 사용할 수 없다.



# 1-4. 관련 함수
print("\n1-4. 관련 함수")

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'} 
print(a.keys()) # key를 모아서 리스트로 만듦.

print(a.values()) # value를 모아서 리스트로 만듦.

print(a.items()) # key value 쌍을 튜플로 묶어 리스트로 반환

print(a.get('name')) # key에 대응하는 value를 반환. key가 존재하지 않으면 오류가 아니라 None 반환.

print(a.get('foo', 'bar')) # 찾으려는 key값이 없을 경우 디폴트값을 대신 출력하도록 할 수 있음. result: bar

print(a.clear()) # 딕셔너리 내부 모든 요소 삭제.



# 2. 집합
print("\n2. 집합")
# 중복을 허용하지 않음
# 순서가 없음
# 인덱싱으로 값을 얻을 수 없음
# 2-1. 생성
print("2-1. 생성")

s1 = set([1,2,3]) 
print(s1) # result : {1, 2, 3}

s2 = set("Hello") 
print(s2) # result : {'e', 'H', 'l', 'o'}   

# 2-2. 교집합/합집합/차집합
print("\n2-2. 교집합/합집합/차집합")
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2) # 교집합

print(s1.intersection(s2)) # 교집합. result : {4,5,6}


print(s1 | s2) # 합집합

print(s1.union(s2)) # 합집합. result : {1,2,3,4,5,6,7,8,9}


print(s1 - s2) # 차집합

print(s1.difference(s2)) # 차집합. result : {1,2,3}


print(s2 - s1) # 차집합

print(s2.difference(s1)) # 차집합. result : {7,8,9}



# 2-3. 관련 함수
print("\n2-3. 관련 함수")

s1 = set([1,2,3])
s1.add(4) # 값 1개 추가
print(s1) # result : {1,2,3,4}

s1 = set([1,2,3])
s1.update([4,5,6]) # 값 여러 개 추가
print(s1) # result : {1,2,3,4,5,6}

s1 = set([1,2,3])
s1.remove(2) # 값 여러 개 추가
print(s1) # result : {1,3}