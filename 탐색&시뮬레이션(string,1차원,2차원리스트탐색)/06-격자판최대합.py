# 격차판 최대합
# 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력

# 각 행의 합 : 11, 12, 13, 14, 15
# 각 열의 합 : 11, 21, 31, 41, 51
# 두 대각선의 합 : 11, 22, 33, 44, 55

import sys
sys.stdin = open('탐색&시뮬레이션(string,1차원,2차원리스트탐색)/in6.txt', "rt")

n = int(input())

col_sum=row_sum=col_idx=0
cross_sum=cross_sum2=0
result = []

for i in range(0, n):
  a = list(map(int, input().split()))

  # 각 행의 합
  result.append(row_sum)
  row_sum = 0
  for j in a:
    row_sum += j

  # 두 대각선의 합
  cross_sum += a[i]
  cross_sum2 += a[n - 1 - i]
  result.append(cross_sum)
  result.append(cross_sum2)

  # 각 열의 합
  while (col_idx < n - 1):
    col_idx += 1
    col_sum += a[col_idx]
    result.append(col_sum)
  
print('result', max(result))

######################################################

a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
  row_sum=col_sum=0
  for j in range(n):
    row_sum += a[i][j]
    col_sum += a[j][i]
  if row_sum > largest:
    largest = row_sum
  if col_sum > largest:
    largest = col_sum

cross_sum1=0
cross_sum2=0
for i in range(n):
  cross_sum1 += a[i][i]
  cross_sum2 += a[i][n-i-1]
  if cross_sum1 > largest:
      largest = cross_sum1
  if cross_sum2 > largest:
    largest = cross_sum2
