import math


class Snow:
    
    def __init__(self, s):
        self.count_snow = int(s)
        
    def __add__(self, n):
        self.count_snow += n
        
    def __sub__(self, n):
        self.count_snow -= n
    
    def __mul__(self, n):
        self.count_snow *= n
        
    def __truediv__(self, n):
        self.count_snow = math.floor(self.count_snow / n)
    
    def makeSnow(self, s, r):
        row = "*" * r
        count_row = s.count_snow / r
        itog = (row + "\n") * int(count_row)
        return itog
    
    def __call__(self, new_value):
        self.count_snow = int(new_value)
        
    def __repr__(self):
        return s.makeSnow(s, 6)
    
        
s = Snow(20)
s + 15
s - 5
s * 15
s / 5
s(29)


print (s)

