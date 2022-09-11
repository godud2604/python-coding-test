# 소수 구하기

n = 20
array = []

for i in range(2, n+1):
  num = 0
  for j in range(2, i+1):
    if i % j == 0:
      num += 1

  if num == 1:
    array.append(i)

print(array) 


