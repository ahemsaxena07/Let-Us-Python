class complex:
    def __init__(self, r, i):
        self.__real = r
        self.__image = i
        def display():
            print(self.__real + self.__image)
            print(self.__real - self.__image)
            print(self.__real * self.__image)
            print(self.__real / self.__image)
        display()          
complex(20, 10)
