arr = [5, 3, 7, 9, 2, 5, 2, 6]

# 최솟값 구하기
min = 100
for idx, item in enumerate(arr):
  if min >= item:
    min = item


##################################################

arrMin = float('inf') # 파이썬에서 가장 큰 값이 저장된다.
for i in range(len(arr)):
  if arr[i] < arrMin:
    arrMin = arr[i]
