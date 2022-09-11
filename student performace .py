marks1= int(input("enter the marks of the subject 1 : "))
marks2= int(input("enter the marks of the subject 2 : "))
marks3= int(input("enter the marks of the subject 3 : "))
average = ((marks1+marks2+marks3)/3)*100

if(average>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("student is pass")
else:
    print('''student is fail''')
        
     