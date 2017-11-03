class Time(object):
    """hour, minute, second"""
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))

time = Time()
#time.print_time()


class Point(object):
    """x,y"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g,%g)'%(self.x,self.y)
    def __add__(self,other):
        if isinstance(other,Point):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other[0]
            self.y += other[1]

    def print_point(self):
        print('(%g,%g)'% (self.x,self.y))

p1 = Point()
p2 = Point()
p2 = (1,2)

p1.__add__(p2)
print(p1)
##print(p1)
##p1.print_point()

#__init__makes it easier to instantiate object and __str__makes it easier to
#debug
#type-based dispatch
