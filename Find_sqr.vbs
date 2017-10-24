Function Newton_sqr(x As Double, TOL As Double) As Double
    'using newton method to find root for f(x) = x*x - 25
    'initial guess to be g, and better guess is
    'g' = g - f(x)/f'(x)
    Dim g As Double
    Dim Num As Long
    g = x / 2
    Num = 1
   Do While Abs(g * g - x) >= TOL
        g = g - ((g * g - x) / (2 * g))
        Num = Num + 1
    Loop
    Debug.Print Num
    Newton_sqr = g
     
End Function

Function EE_sqr(x As Double, step As Double) As Double
    'Using Exhaustive Enumeration method to find square root
    Dim ans As Double, TOL As Double
    Dim Num As Long
    ans = 0
    TOL = step * step
    Num = 1
    Do While Abs(ans * ans - x) >= TOL And ans < x
        ans = ans + step
        Num = Num + 1
    Loop
    Debug.Print Num
    EE_sqr = ans
        
End Function

Function Bisec_sqr(x As Double, TOL As Double) As Double
    'Using besection method to find square root
    Dim ans As Double, hi As Double, lo As Double
    Dim Num As Long
    Num = 1
    hi = x
    lo = 0
    ans = (hi + lo) / 2
    Do While Abs(ans * ans - x) >= TOL
        If ans * ans > x Then
            hi = ans
        Else
            lo = ans
        End If
    Num = Num + 1
    ans = (hi + lo) / 2
    Loop
    
    Debug.Print Num
    Bisec_sqr = ans
End Function

Sub main()
    Dim x As Double, step As Double, TOL As Double
    x = 25
    step = 0.01
    TOL = step * step
    Debug.Print Newton_sqr(x, TOL) '6 steps
    Debug.Print EE_sqr(x, step) '501 steps
    Debug.Print Bisec_sqr(x, TOL) '20 steps
End Sub
