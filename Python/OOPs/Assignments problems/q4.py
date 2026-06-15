from abc import ABC

class Shape(ABC):
    @classmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, r):
        return 3.14*r*r
    
class Rectangle(Shape):
    def area(self,a,b):
        return a*b

class Triangle(Shape):
    def area(self, h,b):
        return h*b/2
    
c1 = Circle()
print(c1.area(7))

r1 = Rectangle()
print(r1.area(5,4))

t1 = Triangle()
print(t1.area(15,8))
