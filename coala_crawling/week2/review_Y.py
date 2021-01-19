num = int(input("시작할 단의 수를 입력하세요:"))

for i in range(num, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)
    print("===============================")