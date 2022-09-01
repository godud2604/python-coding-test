import sys
sys.stdin = open('기본문제/in8.txt', "rt")

n = int(input())
k = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  while x > 0:
    sum += x % 10
    x = x // 10
  return sum

max = -214700000
for x in k:
  tot = digit_sum(x)

  if tot > max:
    max = tot
    res = x

print(res)