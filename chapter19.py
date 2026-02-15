#pro 19.1- write a python program that displays the attributes of integer, float and function objects. also sho whow therse attributes can be used.
def Fun():
    print('everthing is an object')
print(dir(5))
print(dir(-3.4))
print(dir(Fun))
print((5).__add__(6))
print((-5.56).__abs__())
d = globals()
d['Fun'].__call__()

#pro 19.2-
class Date:
    def __init__(self, d, m, y):
        self.__day, self.__mth, self.__yr = d, m, y 
    def __eq__(self, other):
        if self.__day == other.__day and self.__mth == other.__mth and self.__yr == other.__yr:
            return True
        else:
            return False
d1 = Date(17, 11, 98)
d2 = Date(17, 11, 98) 
d3 = Date(19, 10, 92)
print(id(d1))
print(id(d2))
print(d1 == d3)    

#prob 19.3

class Weather:
    def __init__(self):
        self.__param = ['temp', 'rel hum', 'cloud cover', 'wind vel']
    def __contains__(self, p):
        return True if p in self.__param else False
w = Weather()
if 'rel hum' in w:
    print("valid weather parameter")
else:
    print("invalid weather parameter")