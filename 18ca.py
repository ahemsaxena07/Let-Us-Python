# class complex:
#     def __init__(self, r, i):
#         self.__real = r
#         self.__image = i
#         def display():
#             print(self.__real + self.__image)
#             print(self.__real - self.__image
#             print(self.__real * self.__image)
#             print(self.__real / self.__image)
#         display()          
# complex(20, 10)

class complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i
    def display(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {-self.imag}i")

    def add(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def sub(self, other):
        return complex(self.real - other.real, self.imag - other.imag)
    
    def mul(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return complex(real_part, imag_part)
    
    def div(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_ = (self.real * other.real + self.imag * other.imag) / denominator
        imag_ = (self.imag * other.real - self.real * other.imag) / denominator 
        return complex(real_, imag_)

c1 = complex(20, 10) 
c2 = complex(5, 2)
c1.add(c2).display()
c1.sub(c2).display()
c1.mul(c2).display()
c1.div(c2).display()