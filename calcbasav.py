calcul=int(input("entr 1 for continue till 0 number"))
number1=int(input("enter 1st number"))
number2=int(input("enter 2nd number"))
choice=input("enter + for add,- for sub,* for multiply,/ for division")
while calcul==1:
    print(choice)
    if choice=="+":
        print(number1+number2)
    elif choice=="-":
        print(number1-number2)
    elif choice=="*":
        print(number1*number2)
    elif choice=="/":
        print(number1/number)
    break    
calcul = int(input("entr 1 for continue till 0 number"))
