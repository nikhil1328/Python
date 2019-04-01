#25 March 2019
#Written by NIKHIL KULKARNI
#Simple calculator to perform basic oprations.
#print("Python Calculator")

a=float(input("Enter First number: "))
b=float(input("Enter Second number: "))

choice=input("Enter oprator: 1=+, 2=-, 3=* 4=/ : ")

if(choice==1):
    print(a+b)

elif(choice==2):
    print(a-b)

elif(choice==3):
    print(a*b)

elif(choice==4):
    print(a/b)

else:
    print("Invalid Argument, Try Again ")
