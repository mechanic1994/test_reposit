import math


class Roll:
    
    def __init__(self):
        self.length = float(input("Введите длину рулона "))
        self.width = float(input("Введите ширину рулона "))
    def square(self):
        square_roll = self.length * self.width
        return square_roll
        
        
class Win_Door:
    
    def __init__(self):
        self.length = float(input("Введите длину объекта "))
        self.width = float(input("Введите ширину обьекта "))
    def square(self):
        
        #square_wd = x * y
        square_wd = self.length * self.width
        return square_wd
         

class Room:
    
    def __init__(self):
        self.width = float(input("Введите ширину комнаты "))
        self.length = float(input("Введите длину комнаты "))
        self.height = float(input("Введите высоту комнаты "))
        #self.square = 2 * z * (x + y)
        self.wd = []
        
    def square(self):
        #square_room = 2 * z * (x + y)
        square_room = 2 * self.height * (self.length + self.width)
        return square_room
        
    def addWD(self):
        count_object = int(input("Введите количество объектов," 
        " которые требуется вырезать "))
        count = 0
        while count_object != count:
            self.wd.append(Win_Door())
            count += 1
        
    def workSurface(self):
        work_square = Room.square(self)
        for i in self.wd:
            work_square -= i.square()
        return work_square
        
    def how_many_roll(self):
        #square_roll = Roll(l, w).square()
        count_roll = Room.workSurface(self) / Roll().square()
        return math.ceil(count_roll)
        #self.roll.append(Roll(l, w))
        
    def __str__(self):
        return "Площадь стен " + str(r1.square()) + "\n" + \
        "Рабочая поверхность " + str(r1.workSurface()) + "\n" + \
        "Количество рулонов " + str(r1.how_many_roll())
        #return str(r1.workSurface())
        #return str(square_room)

 
r1 = Room()
r1.addWD()
print(r1)
