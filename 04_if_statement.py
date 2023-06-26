# if문

'''
1. 기본 if문
2. in / not in
3. 리스트/튜플/문자열 응용
4. elif
5. 조건부 표현식
'''

# 1. 기본 if문
print("\n 1. 기본 if문")

money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# result : 택시를 타고 가라

money = 2000
if money > 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# result : 걸어 가라

money = 2000
card = True
if money > 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# result : 택시를 타고 가라

score=80
if score >= 60:
    message = "success"
else:
    message = "failure"
# result : success



# 2. in / not in
print("\n2. in / not in")

print(1 in [1,2,3]) # 1이 [1,2,3] 안에 있는가? result : True

print(1 not in [1,2,3]) # 1이 [1,2,3] 안에 있는가? result : True

print('a' in ('a', 'b', 'c')) # result : true

print('k' not in 'python') # result : True



# 3. 리스트/튜플/문자열 응용
print("\n3. 리스트/튜플/문자열 응용")

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# result : 택시를 타고 가라

# 주머니에 돈이 있으면 가만히 있고 없으면 카드를 꺼내라
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")



# 4. elif
print("\n4. elif")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# result : 택시를 타고 가라



# 5. 조건부 표현식
print("\n5. 조건부 표현식")
score = 80
message = "success" if score >= 60 else "failure"