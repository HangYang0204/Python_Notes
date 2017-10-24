#find the square root of 25 with precision 0.01
x = 25
step = 0.1
ans = 0.0
Num = 1

while abs(ans**2 - x) >= step:
    ans += step
    Num += 1

print('After '+ str(Num) + ' Step(s), Find answer = ' + str(ans))

