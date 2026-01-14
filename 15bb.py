#area of radii's in list
lst = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]
l = map(lambda n: f'{(3.14 * (n**2)):.2f}', lst)
print(list(l))

# by importing pi from maths and also including round for decimal
from math import pi
m = map(lambda n: round(pi * (n ** 2), 2), lst)
print(list(m))