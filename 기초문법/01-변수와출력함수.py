a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b) 

a, b = b, a
print(a, b)

# 변수 타입 
a = 12345
print(type(a))
a = 12.21321323
print(type(a))

print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number", a, b, c)
print("number", a, b, c, sep="") # number123
print("number", a, b, c, sep=",") # number,1,2,3
print("number", a, b, c, sep="\n") # 줄바꿈

# 줄바끔 제거 (일렬로 나열)
print(a, end=' ')
print(b, end=' ')
print(c)


