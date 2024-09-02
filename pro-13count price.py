def count(price,note,n):
    while(price>=(n*note)):
        n+=1
    return n-1
price=int(input("Enter Price:-"))
if(price>=10):
  n=count(price,10,1)
  
  print("Note 10  : ",n)
  
if(price>=20):
   n=count(price,20,1)
   print("Note 20 ",n)
   
if(price>=50):
   n=count(price,50,1)
   print("Note 50 ",n)

if(price>=100):
   n=count(price,100,1)
   print("Note 100 ",n)
if(price>=500):
   n=count(price,500,1)
   print("Note 500 ",n)   