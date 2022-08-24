
a = [23, 12, 36, 53, 19]

# enumerate : index와 원소값을 동시에 접근할 수 있는 것
for x in enumerate(a): 
  print(x)
# (0, 23)
# (1, 12)
# (2, 36)
# (3, 53)
# (4, 19)

b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7 # error
# => list와 달리 tuple은 값을 변경할 수 없다.

for index, value in enumerate(a):
  print(index, value)
print()
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19

# all : 모두 참일 때, all 참
if all(60>x for x in a):
  print("Yes")
else:
  print("No")

# any : 한번이라도 참이 있으면, any 참
if any(15>x for x in a):
  print("Yes")
else:
  print("No")

  