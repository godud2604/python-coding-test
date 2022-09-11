array = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]

cnt = 0
sum = 0

for i in array:
  if i == 1:
    cnt += 1
    sum += cnt
  else:
    cnt = 0
  
print(sum)

