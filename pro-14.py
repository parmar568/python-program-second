num=int(input("Enter the number : "))
sum=0
i=1
no=1

while(i<=num):
    sum=0
    for j in range(1,int(no/2)+1):
        if(no%j==0):
            sum=sum+j
            
    if(no==sum):
        print(no)
        i+=1
    no+=1