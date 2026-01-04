# # # # lst = [21, 42, 74, 23, 75, 344]`    ````````````    `
# # # # d = [x * 10 for x in lst ]
# # # # print(d)
 
# # # def square(number):
# # #     print(number ** 2)

# # # square(4)   
# # def add(numone, numtwo):
# #     return numone + numtwo

# # print(add(5,5)) 
# def multiply(p1, p2):
#     return p1 * p2
# print(multiply(9, 4))
# print(multiply('a', 5))
# print(multiply(4, 'c'))

import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
a, c = circle_stats(4)
print(f"area: {a}, circumference: {c}") 