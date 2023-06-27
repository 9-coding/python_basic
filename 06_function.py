# 함수

'''
1. 기본 형식
2. 여러 개의 입력값 받기
3. 매개변수 초기값 설정
4. 기타
'''

# 1. 기본 형식
print("\n1/ 기본 형식")
def add(a, b):
    return a+b
print(3,4) # result : 7

print(b = 5, a = 3) # 매개변수 지정. 순서에 상관없이 사용할 수 있다.

def say(): # 입력값이 없는 함수
    return 'HI'
a = say()
print(a)

def add(a, b): # 결과값이 없는 함수
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3,4)



# 2. 여러 개의 입력값 받기
print("\n2. 여러 개의 입력값 받기")

def add_many(*args): # *를 사용해 여러 개의 입력값을 받을 수 있음.
    result = 0
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3)) # result : 6
print(add_many(1,2,3,4,5,6,7,8,9,10)) # result : 55

def add_mul(choice, *args): # *args를 사용할 때 다른 매개변수도 사용할 수 있음.
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
print(add_mul('add', 1, 2, 3, 4, 5)) # result : 15
print(add_mul('mul', 1, 2, 3, 4, 5)) # result : 120

def print_kwargs(**kwargs): # 키워드 파라미터 사용. kwargs는 딕셔너리가 되고 key=value 형태의 파라미터가 저장된다.
    print(kwargs)
print(print_kwargs(a=1)) # {'a': 1}
print(print_kwargs(name='foo', age=3)) # {'age': 3, 'name': 'foo'}



# 3. 매개변수 초기값 설정
print("\n3. 매개변수 초기값 설정")

def say_myself(name, old, man=True): # 매개변수를 여기에서 초기화할 수 있음. 초기화한 값들은 마지막에 배치.
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
print(say_myself("python", 20)) # print("python", 20, True)와 같은 결과.
print(say_myself("python", 20, False)) # 다른 값을 입력하면 적용됨.



# 4. 기타
print("\n4. 기타")

# global 명령어 사용
# 함수 외부의 전역변수에 접근할 수 있음
a = 1
def vartest():
    global a 
    a = a + 1
vartest()
print(a) # result : 2

# lambda
# 함수 생성 예약어. def 사용할 정도로 복잡하지 않을 때 주로 사용
add = lambda a, b: a+b 
print(3, 4)