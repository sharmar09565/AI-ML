from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, workingDay):
        pass

class Intern(Employee):
    def calculate_salary(self, workingDay):
        intern_salary = workingDay*800
        return intern_salary
    
class FullTimeEmployee(Employee):
    def calculate_salary(self, workingDay):
        intern_salary = workingDay*1200
        return intern_salary
    
i1 = Intern()
print(i1.calculate_salary(30))

ft1 = FullTimeEmployee()
print(ft1.calculate_salary(30))