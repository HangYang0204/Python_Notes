#using Newton method to calculate square root of 25, converting to problem
#Find root for f(x) = x**2 - 25, f'(x) = 2*x
#Giving guess as g, then better guess is g' = g - f(g)/f'(g)
x = 25.0
precision = 0.01
ans = x/2.0
Num = 1

while abs(ans*ans - x) >= precision:
    ans = ans - (((ans**2) - x)/(2*ans))
    Num += 1

print(str(Num) + ' Steps used to find answer = ' + str(ans))