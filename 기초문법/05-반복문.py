# 1. 1부터 N까지 홀수 출력하기
for i in range(1, 10):
  if i % 2:
    print(i)

# 2. 1부터 N까지의 합 구하기
sum = 0
for i in range(1, 11):
  sum += i


# 3. N의 약수 출력하기
x = 10
result = list()
for i in range(1, x + 1):
  if x % i == 0:
    result.append(i)
