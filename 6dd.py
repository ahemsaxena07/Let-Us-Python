i = '12345'
j = i[-1] + i[-2] + i[-3] + i[-4] + i[-5]
print(i)
print(j)

k = sum(int(digit) for digit in i)
print(k)

l = sum(int(digit) for digit in j)
print(l)