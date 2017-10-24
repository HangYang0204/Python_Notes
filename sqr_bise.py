#bisection to find square root of 25
x = 25
precision = 0.01**2
#define lo and hi
lo = 0.0
hi = x
#Giving initial value for the answer between lo and hi
ans = (hi+lo)/2.0
#counter
Num = 1
while abs(ans**2 - x) >= precision:
    if ans**2 < x:
        lo = ans
    else:
        hi = ans
    ans = (hi+lo)/2.0
    Num += 1

print(str(Num) + ' steps used to find answer = ' + str(ans))