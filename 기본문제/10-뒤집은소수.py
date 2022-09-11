list = [32, 55, 62, 3700, 250]

def reverse(arr):
  reverseList = []
  for item in arr:
    reverseList.append(int(str(item)[::-1]))
    
  return reverseList

result = []
def isPrime(list):
  for i in list:
    for j in range(2, i):
      if i % j == 0:
        break
    if i % j != 0:
      result.append(i)
  return result
      
print(isPrime(reverse(list)))

