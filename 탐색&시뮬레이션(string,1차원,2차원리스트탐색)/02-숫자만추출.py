str = 'g0en2Ts8eSoft'
list = list(str)

for i in str:
  if i.isdecimal() == False:
    list.remove(i)

joinList = ''.join(list)
resultNum = int(joinList)

print('자연수 : ', resultNum)

cnt = 0
for i in range(1, resultNum+1):
  if resultNum % i == 0:
    cnt += 1

print('자연수 약수 개수 : ', cnt)

##########################################

res = 0
for x in str:
  if x.isdecimal():
    res = res * 10 + int(x) # 문자열 숫자 누적 합
print('자연수 : ', res)

cnt = 0
for i in range(1, res+1):
  if res % i == 0:
    cnt += 1
print('자연수 약수 개수 : ', cnt)
