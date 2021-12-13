


print("        _________*welcome to mini calculator*________ ")


operator = input("Enter the operator (+,-,*,/,%) : ")
f1= int(input("\nEnter the first number : "))
f2= int(input("Enter the second number : "))

if operator=="+":
        print("Answere is : ",f1+f2)
        
elif operator=="-":
        print("Answere is : ",f1-f2)

elif operator=="*":
        print("Answere is : ",f1*f2)

elif operator=="/":
        print("Answere is : ",f1//f2)

elif operator=="%":
        print("Answere is : ",f1%f2)

else:
    print(" Invalid operation ")
    exit()
