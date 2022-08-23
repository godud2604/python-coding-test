import random as r

a = [1, 2, 3, 4, 5]

a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)

a.pop(3) # 3번 Index의 요소 제거
print(a)

a.remove(4)
print(a)

print(a.index(1)) # 1이라는 요소가 몇 번째 Index에 있는지

print(sum(a))
print(max(a))
print(max(7, 5))

r.shuffle(a) # 랜덤
print(a)