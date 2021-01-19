height = int(input("키(cm)을 입력하세요: "))
weight = int(input("몸무게(kg)을 입력하세요: "))

BMI = (weight / (height * height)) * 10000

print("BMI: ", BMI)