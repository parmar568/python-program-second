
students=int(input("How Many Students : ")) #neter the student 
p=0
i=1
while(i<=students):
    m=int(input("Enter {} Student Marks : ".format(i))) #enter the student marks 
    if(m>=40):
        p+=1
    i+=1    
print("Percantage of Passing Students {}".format((p*100)/students))
    