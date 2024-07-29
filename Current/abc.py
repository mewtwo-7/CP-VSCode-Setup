def fun(a,b):
    # s=0
    # i=a
    # r=b-a+1
    # for x in range(r) :
    #     s=s+i*i*i
    #     i=i+1
    print(-(((a-1)*(a)/2)*((a-1)*(a)/2)-((b)*(b+1)/2)*((b)*(b+1)/2)))


fun(10,1000000000000000)

def fibonacci(n):
    l=[0,1]
    r=1
    if n>2:
        for i in range(n-2):
          k=len(l)
          j=l[k-2]+l[k-1]
          l.append(j)
        print(l)
    elif n==1:
        print([0])
    else :
        print([0,1])
fibonacci(65)   


        


   


