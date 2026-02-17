#containership and inheritance

class Department:
    def set_department(self):
        self.__id = input("enter department id: ")
        self.__name = input("enter department name: ")

    def display_department(self):
        print("department id: ", self.__id)
        print("department name: ", self.__name)
class Employee:
    def set_employee(self):
        self.__eid = input("enter employee id: ")
        self.__ename = input("enter employee name: ")
        self.__dobj = Department()
        self.__dobj.set_department()

    def display_employee(self):
        print("employee id: ", self.__eid)
        print("employee name: ", self.__ename)
        self.__dobj.display_department()
obj = Employee()
obj.set_employee()
obj.display_employee()

