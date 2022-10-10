# 사과나무(다이아몬드)
# N의 크기는 항상 홀수
# 0 => 2
# 1 => 1 2 3
# 2 => 0 1 2 3 4
# 3 => 1 2 3
# 4 => 2

import sys
sys.stdin = open('탐색&시뮬레이션(string,1차원,2차원리스트탐색)/in7.txt', "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2

for i in range(n):
  for j in range(s, e+1):
    res += a[i][j]
  if i < n//2:
    s -= 1
    e += 1
  else:
    s += 1
    e -= 1

print(res)
    