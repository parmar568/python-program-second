#fibonacci sequence 
f=int(input("Enter your number:-"))
pre=1
next=0
sum=0
print("Fibonacci Series : ")
for i in range(f):
    sum=pre+next
    print(sum,end=" ")
    pre=next
    next=sum