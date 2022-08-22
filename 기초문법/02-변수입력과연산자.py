# a = input("숫자를 입력하세요 : ")
# print(a)

# a, b = input("숫자를 입력하세요 : ").split()
# print(type(a)) # str
# c = a + b
# print(type(c)) # str
# print(c) # 23

a, b = map(int, input("숫자를 입력하세요: ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a//b) # 몫 (5 // 2 => 2)
print(a%b) # 나머지 (5 % 2 => 1)
print(a**b)