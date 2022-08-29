from fileinput import close
import sys
sys.stdin = open("기본문제/in5.txt", "rt")

n = input()
k = list(map(int, input().split()))

sum = 0
average = 0
for idx, item in enumerate(k):
  sum += item
  average = sum / int(n)

arrMin = float('inf')
for i in range(len(k)):
  if int(abs(average - k[i])) < arrMin:
    arrMin = k[i]

    if int(abs(average - k[i])) == 0:
      break

findIndex = 0
for idx, item in enumerate(k):
  print(idx, item)
  if arrMin == item:
    findIndex = idx
    break


####################################################

n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a) / n)
min = 21470000000
for idx, x in enumerate(a):
  tmp = abs(x - ave)
  if tmp < min:
    min = tmp
    score = x
    res = idx + 1
  elif tmp == min:
    if x > score:
      score = x
      res = idx + 1
print(ave, res)
