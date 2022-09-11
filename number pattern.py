n=int(input("enter the number : "))

for i in range(1,n+1):
    for n in range(1,n+1):
        if(i==n):
            for j in range(1,n+1):
                print(str(j),end=" ") 
        else:
            print("\n")   