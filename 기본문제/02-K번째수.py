# 6 2 5 3
# 1. 6개의 숫자
# 2. 2번째 부터 5번째 까지
# 3. 오름차순 했을 때, 3번째 숫자 

def result(arr, min, max, findeIndex):
  newArr = arr[min-1:max]
  newArr.sort()

  return newArr[findeIndex-1]

# print(result([5, 2, 7, 3, 8, 9], 2, 5, 3)) # 7
print(result([4, 15, 8, 16, 6, 6, 17, 3, 10, 11, 18, 7, 14, 7, 15], 3, 10, 3)) # 6


#####################################################################################################

import sys
sys.stdin = open("기본문제/in2.txt", "rt") # r: 읽기용, t: 바이너리 모드에 따른 텍스트 모드

T = int(input()) # input() :  파일의 한 줄을 읽어 가져옴

for t in range(T):
  n, s, e, k = map(int, input().split()) 
  a = list(map(int, input().split()))
  a = a[s-1:e]
  a.sort()
  print("#%d %d" %(t+1, a[k-1]))