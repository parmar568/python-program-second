#pro-3 roll number slicing
"""
enter the roll number to dpname,year,degree and rollnumber 
"""
inp = input("enter format: of roll number ")
inp=inp.upper()
branch=inp[0:2]
year=inp[2:4]
degree=inp[4:5]
cp=inp[5:]
if(branch=="CS"):   #check condition to student are cs department 
    branch="Computer Science"
    if(degree=="M"):
        degree="MCA"
    elif(degree=="B"):
        degree="BCA"
    else:
        degree="PGDCA"
elif(branch=="ME"): #check condition to student are mechanical  department 
    branch="Mechanical engineering"
    if(degree=="B"):
        degree="BME"
    else:
        degree="MME"
print("Branch : {} , Year : 20{} , Degree : {} , RollNo : {}".format(branch,year,degree,cp))