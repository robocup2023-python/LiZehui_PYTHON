'''
第九天
Author：李泽辉
2221313156
'''
import math

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"创建了Point({self.x}, {self.y}, {self.z})")
    
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Point类只能与Vector类相加")
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Point类只能与Vector类相减")
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __lt__(self, other):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2) < math.sqrt(other.x**2 + other.y**2 + other.z**2)
    
    def __gt__(self, other):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2) > math.sqrt(other.x**2 + other.y**2 + other.z**2)
    
    def __del__(self):
        print(f"销毁了Point({self.x}, {self.y}, {self.z})")


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"创建了Vector({self.x}, {self.y}, {self.z})")
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, x):
        radian = math.radians(x)
        x_new = self.x * math.cos(radian) - self.y * math.sin(radian)
        y_new = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(x_new, y_new, self.z)
    
    def __truediv__(self, x):
        radian = math.radians(x)
        x_new = self.x * math.cos(radian) + self.y * math.sin(radian)
        y_new = -self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(x_new, y_new, self.z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __del__(self):
        print(f"销毁了Vector({self.x}, {self.y}, {self.z})")


# 测试代码
p1 = Point(1, 2)
p2 = Point(3, 4)
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(p1 + v1)
print(p2 - v2)
print(p1 - p2)
print(p1 == p2)
print(p1 < p2)
print(p1 > p2)

v3 = v1 * 90
print(v3)

v4 = v2 / 90
print(v4)

del p1
del p2
del v1
del v2
