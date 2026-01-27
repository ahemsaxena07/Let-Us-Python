# #classes and objects
# class Employee:
#     def set_data(self, n, a, s):
#         self.name = n
#         self.age = a
#         self.salary = s

#     def display_data(self):
#         print(self.name, self.age, self.salary)

# e1 = Employee()
# e1.set_data('Ramesh', 23, 25000)
# e1.display_data

class person:
    def __init__(self, n, o):
        print('hey im a person')
        self.name = n
        self.occupation = o
    def info(self):
        print(f'{self.name} is the {self.occupation}')
a = person('ahem', 'founder and ceo')
b = person('aditi', 'ahems wife')
a.info()
b.info()

# import math
# import functions
# a = 125
# b = 'spooked'
# # print(vars())
# # print(vars(math))
# # print(dir())
# # print(dir(math))
# print(dir(functions))

# class Fruit:
#     count = 0
#     def __init__(self,name = '', size = 0, color =''):
#         self.name = name
#         self.size = size
#         self.color = color
#         Fruit.count += 1

#     def display():
#         print(Fruit.count)
# f1 = Fruit('Banana', 5, 'Yellow')
# print(vars(Fruit))
# print(dir(Fruit))
# print(vars(f1))
# print(dir(f1))

#prob 18.1
class number:
    def set_number(self,n):
        self.__num = n

    def get_number(self):
        return self.__num
    
    def print_number(self):
        print(self.__num)

    def isnegative(self):
        if self.__num<0:
            return True
        else:
            return False
        
    def isdivisibleby(self,n):
        if n == 0:
            return False
        if self.__num % n == 0:
            return True
        else:
            False
            
    def absolute_value(self):
        if self.__num >= 0:
            return self.__num
        else:
            return - 1 * self.__num

x = number()
x.set_number(-1234)
x.print_number()
if x.isdivisibleby(5) == True:
    print('5 divides', x.get_number())
else:
    print('5 does not divide', x.get_number())
print('absolute value of', x.get_number(), 'is', x.absolute_value())

#prob 18.2
class Fruit:
    count = 0
    def __init__(self, name = '', size = 0, color = ''):
        self.__name = name
        self.__size = size
        self.__color = color
        Fruit.count += 1
    def display():
        print(Fruit.count)
f1 = Fruit('banana', 3, 'yellow')
f2 = Fruit('apple',  4, 'red')
f3 = Fruit('orange', 5, 'red')
Fruit.display()
print(Fruit.count)  

#prob 18.3
class complex:
    def __init__(self, r = 0.0, i = 0.0):
        self.__real = r
        self.__image = i
    def __eq__(self, other):
        if self.__real == other.__real and self.__iamge == other.__image:
            return True
        else:
            return False
c1 = complex(0.2,0.1)
c2 = complex(1.2, 3.3)
c3 = c1
if c1 == c2:
    print("Attributes of c1 and c2 are same.")
else:
    print("Attribute of c1 and c2 are different.")
if type(c1) == type(c3):
    print("c1 and c3 are of same type")
else:
    print("c1 and c3 are of different type")
if c1 is c3:
    print('c1 and c3 are pointing to same object')
else:
    print('c1 and c3 are pointing to different objects')

#prob 18.4
import builtins
print(dir(builtins))
print()
print(vars(builtins))

#prob 18.5
def msg1():
    print("hello my name is ahem")
def msg2():
    print("The CEO and Founder of The Starbase")
d = vars()
i = dir()
print(sorted(d.keys()))
print(i)
print(d.keys() - i)
print(i - d.keys())