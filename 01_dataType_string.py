# 문자열

'''
1. 대입
2. 숫자와 함께 대입
3. format 함수 이용
4. f 문자열 포매팅
5. 문자열 관련 함수
'''

# 1. 대입
print("1. 대입")

print("I eat %d apples." % 3)

n = 3
print("I eat %d apples." % n)

print("I eat %s apples." % "five")

num = 10
day = "three"
print("I age %d apples. so I was sick for %s days." % (num, day))

#  %s : 문자열  |  %c : 문자 1개  |  %d : 정수  |  %f : 실수  |  %o : 8진수  |  %x : 16진수  |  %% : % 문자  |



# 2. 숫자와 함께 대입
print("\n2. 숫자와 함께 사용")

print("%10s" % "hi") # %10s : 전체 길이가 10인 문자열 공간에서 대입되는 값을 오른쪽 정렬.

print("%-10sjane" % "hi") # %-10s : 왼쪽 정렬.

print("%0.4f" % 3.141592) # 소수점 4번쨰 자리까지만 나타냄.

print("%10.4f" % 3.141592) # 소수점 4번째 자리까지만 표시, 전체 길이가 10인 문자열 공간에서 오른쪽 정렬.



# 3. format 함수 사용
print("\n3. format 함수 사용")

print("I eat {0} apples.".format(3)) # 숫자 대입

n = 3
print("I eat {0} apples.".format(n)) # 숫자 변수 대입

print("I eat {0} apples.".format("five")) # 문자열 대입

num = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(num, day)) # 2개 이상의 값 넣기

print("I ate {num} apples. so I was sick for {day} days.".format(num=10, day=3)) # 이름으로 넣기

print("{0:<10}".format("hi")) # 문자열을 10자리로 맞추고 왼쪽 정렬

print("{0:>10}".format("hi")) # 문자열을 10자리로 맞추고 오른쪽 정렬

print("{0:^10}".format("hi")) # 문자열을 10자리로 맞추고 가운데 정렬

print("{0:=^10}".format("hi")) # 공백 채우기 - 문자를 가운데에 놓고 '='로 채우기

print("{0:!<10}".format("hi")) # 공백 채우기 - 문자를 왼쪽에 놓고 '!'로 채우기

n = 3.141592
print("{0:0.4f}".format(n)) # 소수점 4자리까지만 표시

print("{0:0.4f}".format(n)) # 자릿수를 10으로 맞추고 소수점 4자리까지만 표시



# 4. f 문자열 포매팅
print("\n4. 문자열 포매팅")

name = 'python'
age = 20
print(f"my name is {name}, and my age is {age}") # f 문자열 포매팅

print(f"my name is {name}, and my age is {age+1}") # 연산 가능.



# 5. 문자열 관련 함수
print("\n5. 문자열 관련 함수")

a = "hobby"
print(a.count('b')) # 문자열 중 문자 b의 개수 반환

s = "Python is the best choice"
print(s.find('b')) # 문자열에서 b가 처음 나온 위치

print(s.find('k')) # 없으면 -1 반환

s = "Life is too short"
print(s.index("t")) # t의 위치 반환

print(",".join('abcd')) # 문자열 삽입. abcd 사이에 , 삽입

print(",".join(['a','b','c','d'])) # 리스트 사용해 문자열 삽입. abcd 사이에 , 삽입

a = "hi"
print(a.upper()) # 소문자를 대문자로.

a = "HI"
print(a.lower()) # 대문자를 소문자로.

a = " HI "
print(a.lstrip()) # 왼쪽 공백 지우기

print(a.rstrip()) # 오른쪽 공백 지우기

print(a.strip()) # 양쪽 공백 지우기

s = "Life is too short"
print(s.replace("Life", "Your leg")) # replace(바뀔 문자열, 바꿀 문자열) 사용해 문자열 바꾸기

print(s.split()) # 공백을 기준으로 문자열 나누기

b = "a:b:c:d" 
print(b.split(':')) # 기호 기준으로 문자열 나누기