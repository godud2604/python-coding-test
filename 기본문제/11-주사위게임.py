array = [5, 2, 6]

def numDetermination(array):
  cnt = 1
  number = 0
  maxNum = -127000
  for i in range(0, len(array)-1):
    if array[i] == array[i+1]:
      cnt += 1
      number = array[i]

    if array[i] != array[i+1]:
      if maxNum < array[i]:
        maxNum = array[i]
      if maxNum < array[i+1]:
        maxNum = array[i+1]
  return [cnt, number, maxNum]

def amount(resultArr):
  cnt, number, maxNum = map(int, resultArr)

  if cnt == 3:
    return 10000 + (number * 1000)
  if cnt == 2:
    return 1000 + (number * 100)
  if cnt == 1:
    return maxNum * 100
  
print(amount(numDetermination(array)))