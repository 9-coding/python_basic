# 반복문

'''
1. while문
2. for문
  2-1. 기본 형식
  2-2. range()
  2-3. 리스트 내포
'''

# 1. while문
print("1. while문")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

coffee = 5
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피 나왔습니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")   
        print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)



# 2. for문
# 기본 구조 : for 변수 in 리스트/튜플/문자열
print("\n2. for문")
# 2-1. 기본 형식
print("2-1. 기본 형식")

list = ['one', 'two', 'three']
for i in list:
    print(i)
# result : 리스트 안의 요소 한 줄씩 출력

a = [(1,2), (3,4), (5,6)]
for (first, last) in a: # 리스트의 요소가 튜플이므로 각각의 요소가 자동으로 (first, last) 변수에 대입된다.
    print(first + last)
'''
result
3   -> 1+2
7   -> 3+4
11  -> 5+6
'''

# 60점을 기준으로 합격/불합격 결과 반환
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks: # 리스트 안의 요소를 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        print("%d번 학생 합격" % number)
    else:
        print("%d번 학생 불합격" % number)

# 60점을 기준으로 합격만 결과 반환
print("")
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks: # 리스트 안의 요소를 순서대로 mark에 대입
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 합격" % number)



# 2-2. range()
print("\n2-2. range()")

# 1부터 10까지 더하기
result = 0
for i in range(1, 11): # 마지막 숫자는 포함하지 않음
    result = result + i
print(result) # 55

marks = [90, 25, 67, 45, 80]
for num in range(len(marks)): 
    if marks[num] < 60:
        continue
    print("%d번 학생 합격" % (num+1))

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print('')



# 2-3. 리스트 내포
# [표현식 for 항목 in 반복 가능 객체 if 조건]
print("\n2-3. 리스트 내포")

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]

# 짝수에만 곱.
result = [num * 3 for num in a if num % 2 ==0]
print(result) # [6, 12]

# 구구단 리스트에 담기
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)