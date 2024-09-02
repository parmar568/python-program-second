inp = input("enter roll number:-")  #enter the roll number to this format{cs-year-degree-roll number}
inp=inp.upper()
branch=inp[0:2]
year=inp[2:4]
degree=inp[4:5]
cp=inp[5:]
if(branch=="CS"):
    branch="Computer Science"
    if(degree=="M"):
        degree="MCA"
    elif(degree=="B"):
        degree="BCA"
    else:
        degree="PGDCA"
    print("Student  from CS Department")
    print("Branch : {} , Year : 20{} , Degree : {} , RollNo : {}".format(branch,year,degree,cp))
else:
    print("Student is not from CS Department")