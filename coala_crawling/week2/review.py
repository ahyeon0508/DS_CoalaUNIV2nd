num = int(input("줄 수를 입력하세요: "))

for i in range(1, num):
    print("*" * i)

for i in range(num, 0, -1):
    print("*" * i)