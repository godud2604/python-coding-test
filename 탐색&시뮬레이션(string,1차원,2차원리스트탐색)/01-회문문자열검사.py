str = 'Level'

length = len(str) - 1
result = "YES"

for idx, item in enumerate(str):
  a = str[idx].lower()
  b = str[length-idx].lower()

  if a != b:
    result = "NO"

print(result)

################################################

import sys
sys.stdin = open('탐색&시뮬레이션(string,1차원,2차원리스트탐색)/in1.txt', "rt")

n = int(input())

for i in range(n):
  s = input()
  s = s.upper()
  
  if s == s[::-1]:
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))
