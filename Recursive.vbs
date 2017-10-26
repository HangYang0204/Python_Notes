Function countdown(n As Integer)
    If n < 0 Then
        Debug.Print ("BlastOff")
        Exit Function
    End If
    
    Debug.Print n
    
    Call countdown(n - 1)
    
End Function


Function print_n(s As String, n As Integer)
    If n <= 0 Then
        Exit Function
    End If
    
    Debug.Print s
    
   Call print_n(s, n - 1)
 
End Function


Sub main()
    Dim k As Integer, num As Integer
    Dim t As String
    k = Int(InputBox("enter number you want to countdown: "))
    Call countdown(k)
    t = InputBox("enter string you want to repeat: ")
    num = Int(InputBox("enter number you want to repeat: "))
    Call print_n(t, num)

End Sub
