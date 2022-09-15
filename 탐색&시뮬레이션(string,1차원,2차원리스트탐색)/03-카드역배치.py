import sys
sys.stdin = open('탐색&시뮬레이션(string,1차원,2차원리스트탐색)/in3.txt', "rt")

a = list(range(21))

for _ in range(10):
  s, e = map(int, input().split())
  print(s, e)
  for i in range((e-s+1)//2):
    a[s+i], a[e-i] = a[e-i], a[s+i]
  
a.pop(0) 
for x in a:
  print(x, end=" ")