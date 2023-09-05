
a=input("Enter first number:")
operator=input("Enter operator(+,-,*,%,/): ")
b=input("Enter second number:")

a=float(a)
b=float(b)


if operator =="+":
  print(" "+str(a)+"+ "+str(b)+"= "+str(a+b))

elif operator=="-":
    print(" "+str(a)+"+ "+str(b)+"= "+str(a-b))  

elif operator=="*":
   print(" "+str(a)+"+ "+str(b)+"= "+str(a*b))

elif operator=="%":
   print(" "+str(a)+"+ "+str(b)+"= "+str(a%b))

elif operator=="/":
   if b!='0':
    print(" "+str(a)+"+ "+str(b)+"= "+str(a/b))   

else:
   print("Invalid operation")