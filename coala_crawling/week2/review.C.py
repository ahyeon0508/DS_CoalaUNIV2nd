data=["딸기 : 3362", "바나나 : 3872", "포도 : 3540", "키위 : 3256",
      "참외 : 3784", "수박 : 3987", "망고 : 3423", "복숭아 : 3585", "사과 : 3178"]

# Lv1
for i in data:
    i = i[5:]
    print(i.strip())

# LV2
sum = 0
for i in data:
    i = int(i[5:])
    sum = sum + i
mean = sum / len(data)
print("총 합:", sum)
print("평균:", mean)

# LV3
print("최대값:", max(data).strip()[5:])