# 숫자의 연산
a = 1
b = 5
print(a + b)

c = a - b
print(c)

c = b % 2
print(c)

c = b // 2
print(c)

c = b / 2
print(c)

# 문자의 연산
a = "Hello"
b = "World"
print (a+b) # ,와 달리 공백 없음

print (a*3)

# 문자와 숫자 더하기
a = 100
b = "원"
# print(a+b) # int와 str은 같이 못 더함
a = str(a)
print(a+b)
