name=input("이름 입력: ")
print(name)

age=int(input("나이 입력: "))
print(age+1)

hobbies=input("취미를 ,로 구분해서 입력: ").split(",")
for hobby in hobbies:
    print(hobby)