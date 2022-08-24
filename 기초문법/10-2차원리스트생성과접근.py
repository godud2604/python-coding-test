a = [0] * 10
print(a)

a = [[0] * 3 for _ in range(3)]
print(a) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in a:
  for y in x:
    print(y, end=' ')
  print()