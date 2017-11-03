#wreite a function to calculation distance between two point
import math
import copy

class Point(object):
    """Represents a point in 2-D space. """


def _distince_(p1,p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

p1 = Point()
p2 = Point()

p1.x = 1
p1.y = 2
p2.x = 3
p2.y = 4

#write a function to print the point object like (a,b)
def _print_point_(p):
    print('(%g,%g)' % (p.x,p.y))


#print(p1.z)
#print(_distince_(p1,p2))

#write a function to move a rect
class rect(object):
    """Width, Height, Corner"""

box = rect()
box.width = 1
box.height = 2
box.corner = Point()
box.corner.x = 1
box.corner.y = 1
#Here corner is a point object, this is called embeded.
def _moverect_(rectangles,dx,dy):
    rectangles.corner.x += dx
    rectangles.corner.y += dy
    return rectangles.corner

#write a function to move rect by create a new one instead of update the input
def _moverectv2_(rectangles,dx,dy):
    rectanglescopy = copy.deepcopy(rectangles)
    #rectanglescopy = copy.copy(rectangles)
    rectanglescopy.corner.x += dx
    rectanglescopy.corner.y += dy
    return rectanglescopy.corner
#compare difference between copy and deepcopy
_print_point_(_moverectv2_(box,2,1))
_print_point_(box.corner)


