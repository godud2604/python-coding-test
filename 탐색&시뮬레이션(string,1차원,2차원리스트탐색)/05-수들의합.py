# 투 포인터를 이용하여 해결
# => 좌, 우 방향의 인덱스를 이용하여 한 번의 배열 탐색으로 두 수의 합이 x가 되는 쌍을 찾는다.

# tot : lt 부터 rt 이전 index 사이의 연속 부분 합
# lt indxt => 0, rt index => 1
# m => 3, tot => 1, n => 8

# tot가 m보다 작으면 rt index++ 더해줌
# rt index 증가 => 2
# tot는 lt 부터 rt 전까지의 합 => 0 ~ 1

# tot가 m과 같으면 cnt += 1 
# tot에서 lt와 같은 값을 없애줌
# lt index 증가 => 1

# tot가 m보다 크면
# tot에서 lt와 같은 값을 없애줌
# lt index 증가 => 1

# rt가 n보다 크면, break

import sys
sys.stdin = open('탐색&시뮬레이션(string,1차원,2차원리스트탐색)/in5.txt', "rt")


n, m = map(int, input().split())
a = list(map(int, input().split()))
print(n, m)
print(a)
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
  if tot < m:
    if rt < n:
      tot += a[rt]
      rt += 1
    else:
      break
  elif tot == m:
    cnt += 1
    tot -= a[lt]
    lt += 1
  else:
    tot -= a[lt]
    lt += 1