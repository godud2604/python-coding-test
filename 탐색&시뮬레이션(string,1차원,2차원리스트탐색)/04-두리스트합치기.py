import sys
sys.stdin = open('탐색&시뮬레이션(string,1차원,2차원리스트탐색)/in4.txt', "rt")

# sort => 시간복잡도 nlogn => 10개, 7개 => 17log17 
# 이미 정렬이 되어있는 것 => 시간복잡도 n

# 1. a배열과 b배열과 c배열이 있다.
# 2. a배열의 index 0 =>  p1 / b배열의 index 0 => p2
# 3. p1과 p2를 비교해서 작은 값이 c배열에 append
# 4. 만약, p1이 작은 값으라면 p1은 index 1을 가리킴
# 5. 반복
# 6. 만약, p1과 p2 둘 중, 각 배열의 마지막 index에 도달 했을 때, break
# 7. 마지막 index의 도달한 배열이 아닌 배열 => 나머지 c배열에 append (이미 오름차순 되어있는 상태)

p1=p2=0
c = []

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

while p1 < n and p2 < m:
  if a[p1] <= b[p2]:
    c.append(a[p1])
    p1 += 1
  else:
    c.append(b[p2])
    p2 += 1
if p1 < n:
  c = c + a[p1:]
if p2 < n:
  c = c + b[p2:]

for x in c:
  print(x, end=' ')