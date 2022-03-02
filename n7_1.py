from abc import abstractmethod
from operator import length_hint
from posixpath import split

class Point:
    def __init__(self,x,y):
      self.x = float(x)
      self.y = float(y)
      
point = Point(2,4)

print(point.x, point.y)

class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return (dx**2 + dy**2)**0.5

    
line = Line(point,Point(5,6))
print(line.length())
        
point.x = 0
point.y = 0

print(line.length())



class Point3D(Point):
    def __init__(self, x, y, z):
        self.z = float(z)
        super().__init__(x, y)

point3D = Point3D(2,5,6)

class Shape:
    def __init__(self):
        pass
    @property
    @abstractmethod
    def area(self):
        pass
    @property
    @abstractmethod
    def perimeter(self):
        pass

class Square(Line,Shape):
    def __init__(self,p1,p2):
        super().__init__(p1,p2)

    @property
    @abstractmethod
    def area(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return abs(dx*dy)
    @property
    @abstractmethod
    def perimeter(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return (abs(dx)+abs(dy))*2

square = Square(Point(5,6),Point(7,8))

print(square.area)
print(square.perimeter)


class Rect(Shape):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        super()

    @property 
    @abstractmethod   
    def area(self):
        dx = self.p1.x - self.p2.x
        return abs(dx**2)

    @property
    @abstractmethod
    def perimeter(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return (abs(dx)+abs(dy))*2

rect = Rect(Point(4,5),Point (7,8))
print(rect.area)
print(rect.perimeter)

class Cube(Square):
    def __init__(self, p1, p2, p3):
        self.p3 = p3
        super().__init__(p1, p2) 



    def volume(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        dz = self.p1.z - self.p3.z
        return abs(dx*dy*dz)

cube = Cube(Point3D(2,3,2),Point3D(6,7,3),Point3D(8,5,4))
print(cube.volume())   

   



        


        






    