#1)
class String:
    def _init_(self, chars):
        self.chars = chars

    def getString(self):
        return self.chars

    def uppercase(self):
        return self.chars.upper()

#S1 = String("Ersultan")
#S2 = String("Beibarys")
#print(S1.getString(), S2.getString(), end = '')
#print(sep = "\n")
#print(S1.uppercase(), S2.uppercase(), end = '')

#2)
class Shape:
    def _init_(self, area):
        self.area = 0
    
    def get_area(self):
        return self.area

class Square(Shape):
    def __init__(self, x, area):
        self.lenth = x
        super().__init__(area)

    def area(self):
        print(self.lenth * self.lenth)

class Rectangle(Shape):
    def __init__(self, area, a, b):
        super().__init__(area)
        self.a_side = a
        self.b_side = b

    def area2(self):
        print(self.a_side * self.b_side)


#S1 = Rectangle(5, 2, 0)
#S2 = Rectangle(4, 3, 0)
#print (S1.get_area(), S2.get_area(), sep = '\n')

#4)
import math
class Point:
    def _init_(self, a,b):
        self.a = a
        self.b = b
    def show(self):
        print(self.a, self.b)

    def move(self, x, y):
        self.a, self.b = x, y

    def dist(self, d):
        return math.sqrt(((self.a - d.a)**2 + (self.b - d.b)**2))
    
#l = Point(1, 2)
#m = Point(4, 5)
#print(l.dist(m))

class Account:
    def __init__(self, name, soname, balance):
        self.name = name
        self.soname = soname
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money

    def withdraw(self, unmoney):
        if unmoney < 0: print('wrong number')
        elif self.balance - unmoney < 0: print('Недостаточно средств для снятия')
        else: self.balance = self.balance - unmoney

    def show_balance(self):
        print(self.balance)

import math
def filter_prime(arr):
    l = []
    for i in arr:
        ok = True
        num = int(math.sqrt(i))
        for j in range(2, num+1):
            if i % j == 0:
                ok = False
                break
        if ok == True:
            l.append(i)    
    return l

arr = list(map(int, input().split()))
#print(filter_prime(arr))

filter = lambda list: filter_prime(list)
print(filter([2,3,4,5,6,7,8,9]))