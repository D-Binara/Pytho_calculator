store = []

def enternum():
    global a
    global b
    special_characters = "$"
    
    a = input("Enter first number: ")
    print(a)

    if any(c in special_characters for c in a):
        return -1
    
    if a =='#':
        return -2

    b = input("Enter second number: ")
    print(b)

    if any(c in special_characters for c in b):
        return -1
    
    if b =='#':
        return -2

    a= float(a)
    b= float(b)


def history():
    if len(store) == 0:
        print("No past calculations to show")
    else:
        for calculation in store:
            print(calculation)


def select_op(choice):
    global store
    if choice =='#':
        return -1
    elif choice =='?':
        history()
    
    else:
        enternum_result = enternum()

        if enternum_result == -1:
            return 0
        elif enternum_result == -2:
            return -1

        if choice =='+':
            print(f"{a} + {b} = {a+b}")
            store.append(f"{a} + {b} = {a+b}")
        elif choice =='-':
            print(f"{a} - {b} = {a-b}")
            store.append(f"{a} - {b} = {a-b}")
        elif choice =='*':
            print(f"{a} * {b} = {a*b}")
            store.append(f"{a} * {b} = {a*b}")
        elif choice =='/':
            if b==0:
                print("float division by zero")
                print(f"{a} / {b} = None")
                store.append(f"{a} / {b} = None")
            else:
                print(f"{a} / {b} = {a/b}")
                store.append(f"{a} / {b} = {a/b}")
        elif choice =='^':
            print(f"{a} ^ {b} = {a^b}")
            store.append(f"{a} ^ {b} = {a^b}")
        elif choice =='%':
            print(f"{a} % {b} = {a%b}")
            store.append(f"{a} % {b} = {a%b}")
        else :
            print("Unrecognized operation")
        

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")  
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("9.History  : ?")
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice)  ==-1):
    
    print("Done. Terminating")
    exit()