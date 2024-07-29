def TOTDIS(x1,x2,x3):
    l=[x1,x2,x3]
    l.sort()
    y=x1-x3

   
    print(y)                    

x=int(input("enter number of testcases"))
for i in range (x):
    x1=int(input("enter first integer from 1 to 10"))
    x2=int(input("enter second integer from 1 to 10"))
    x3=int(input("enter third integer from 1 to 10"))
    TOTDIS(x1,x2,x3)
    
 
