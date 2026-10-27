from abc import ABC, abstractmethod

class Employer(ABC):

    def salary(self):
        pass

class Emp(Employer):

    def salary(self):
        return 30000

class Emp1(Employer):

    def salary(self):
        return 10000

class Emp2(Employer):

    def salary(self):
        return 20000

obj=Emp()
print(obj.salary())

obj1=Emp1()
print(obj1.salary())

obj2=Emp2()
print(obj2.salary())