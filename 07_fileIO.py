# 파일 입출력

'''
1. 파일 생성
2. 파일 쓰기
3. readline() / readlines() / read()
4. 파일 내용 추가
'''

# 1. 파일 생성
print("\n1. 파일 생성")

f = open("text.txt", 'w')
f.close()
# 파일 열기 모드 | r : 읽기 모드 | w : 쓰기 모드 | a : 추가 모드



# 2. 파일 쓰기
print("\n2. 파일 쓰기")

f = open("text.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data) # data를 파일 객체 f에 써라
f.close()



# 3. readline() / readlines() / read()
print("\n3. readline() / readlines() / read()")

f = open("text.txt", 'r')
line = f.readline() # 파일의 한 줄 읽어서 저장
print(line)
f.close()

f = open("text.txt", 'r')
# 반복문을 사용하여 모든 줄 출력
while True:
    line = f.readline() 
    if not line: # 파일의 끝에서 반복문 탈출
        break
    print(line)
f.close()

f = open("text.txt", 'r')
lines = f.readlines() # 파일의 모든 줄 읽어서 저장
for line in lines:
    print(line)
f.close()

f = open("text.txt", 'r')
data = f.read() # 파일 내용 전체를 문자열로 반환
print(data)
f.close()



# 4. 파일 내용 추가
# 파일에 원래 존재하던 값을 유지하면서 새로운 값 추가

print("\n4. 파일 내용 추가")

f = open("text.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data) # 파일 내에는 이전 내용에 이어 20개의 줄이 있음을 확인
f.close()

with open("text.txt", "w") as f:
    f.write("Life is too short, you need python")
# with 블록을 벗어나는 순간 f.close()가 자동으로 된다.