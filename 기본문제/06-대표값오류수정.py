# round는 round_half_even 방식을 택한다. 
# => half 일 때, 가까운 짝수로 변환됨
# => 일반적인 수학 개념과 다름

a = 4.500
print(round(a)) # 4

b = 5.500
print(round(b)) # 6

c = 7.500
print(round(c)) # 8

d = 7.400
print(round(d)) # 7

