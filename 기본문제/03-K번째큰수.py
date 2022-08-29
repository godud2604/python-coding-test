import sys
sys.stdin = open("기본문제/in3.txt", "rt")

T = list(map(int, input().split()))
A = list(map(int, input().split()))
setArr = set(A)
listSetArr = list(setArr)
listSetArr.sort()
print(listSetArr[2])

####################################################################################

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
  for j in range(i+1, n): # 1~10
    for m in range(j+1, n):
      res.add(a[i]+a[j]+a[m])

res = list(res)
res.sort(reverse=True)
print(res)
print(res[k-1])
