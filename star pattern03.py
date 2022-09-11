n = int(input("enter the number : "))

for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*((2*i)+1))
    print(" "*(n-i-1))