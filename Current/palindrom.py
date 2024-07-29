def palindrome(s):
  l=len(s)
  check=0
  i=0
  if l%2==0:
    while i<(l/2):
        if s[i]==s[l-i-1]:
            check+=1
        else:
            pass
        i=i+1 
    if check==l/2:
        print("YES")
    else :
        print("NO")
  else:
    while i<((l-1)/2):
        if s[i]==s[l-i-1]:
            check+=1
        else:
            pass
        i=i+1
    if check==((l-1)/2):
        print("YES")
    else:
        print("NO")        
      

palindrome("polihuygtfuhilop")                 



      
    
