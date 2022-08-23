from curses.ascii import isupper


msg = "It is Time"
print(msg.upper())
print(msg.lower())

print(msg.find('T'))
print(msg.count('e'))
print(msg[:2])
print(len(msg))

for x in msg:
  if x.isupper():
    print(x, end= ' ')

print()

for x in msg:
  if x.isalpha(): 
    print(x, end="")

for x in msg:
  print(ord(x)) # ord : 아스키 문자 출력 => A(65) ~ Z(90)


number = 65
print(chr(number)) # 아스키 문자를 대응되는 문자로 출력 (65 => A)