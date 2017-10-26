#write a function to return the area of a circle
import math
def _area_(r):
    temp = math.pi * (r**2)
    return temp

#write a function to return the absolute value of the input
def _abs_(x):
    if x < 0:
        return -x
    else:
        return x

#write a function to return 1 if x > y else - 1
def _bigger_(x,y):
    if x > y:
        return 1
    elif x ==y:
        return 0
    else:
        return -1

#write a function to return the hypotenuse of a right triangle
def _hypotenuse_(x,y):
    temp = x**2 + y**2
    return math.sqrt(temp)

#write a function to calculate the distince
def _distance_(x1,y1,x2,y2):
    temp =(x2-x1)**2 + (y2-y1)**2
    return math.sqrt(temp)

#wwrite a function to return the circle given tow point
def _circle_(x1,y1,x2,y2):
    return _area_(_distance_(x1,y1,x2,y2))

#write a function to check if x is divisible by y
def _isDivisible_(x,y):
    return x % y == 0

#write a function return true is x <= y <= z
def _isBetween_(x,y,z):
    return x<=y<=z

#write a function to calculate factorial of n
def _factorial_(n):
    if n ==0:
        return 1
    else:
        return n*_factorial_(n-1)

#write a function to calculate fibonacci of n
def _fibonacci_(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return _fibonacci_(n-1)+_fibonacci_(n-2)





