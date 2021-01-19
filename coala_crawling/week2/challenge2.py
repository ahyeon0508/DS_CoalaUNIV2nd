data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum = 0

for i in range(len(data)):
    print(data[i])

for i in range(len(data)):
    data[i] = data[i].replace(",", "")[5:]
    print(data[i])

for i in range(len(data)):
    sum = sum + int(data[i])

print("총 합: ", sum)