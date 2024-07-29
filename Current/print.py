
def S(a):
    i=10
    s=0
    while a%i==0:
        s=s+(a%i)
        i=i*10
    return s    


for i in range(2500):
     m=4*(i)
     for j in range(2500):
         n=4*(j)
         if (S(n))*(S(n))==m and (S(m))*(S(m))==n:
             print(m,n)
for i in range(2500):
     m=4*(i)+1
     for j in range(2500):
         n=4*(j)+1
         if (S(n))*(S(n))==m and (S(m))*(S(m))==n:
             print(m,n)             
                     


