class area:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area1(self):
        return self.l*self.b
area2 =  area(10,2)
print(area2.area1())

class cube_area:
    def __init__(self, s):
        self.s = s
    def calculate_area(self):
        return self.s ** 3
area = cube_area(90)
print(area.calculate_area())
