def menu():
    print("\n")
    print("------MENU-----")
    print("ADD NUMBER --- 1")
    print("SUBSTRACT --- 2")
    print("MULTIPLY --- 3")
    print("DIVIDE --- 4")
    print("LEAVE ----> 0")
    print("--------------")
    print("\n")
    
    return int(input("CHOOSE THE METHOD: "))


def add():
    a = int(input("INSERT THE FIRST NUMBER: "))
    b = int(input("INSERT THE SECOND NUMBER: "))

    print("THE RESULT IS", a+b)

def substract():
    a = int(input("INSERT THE FIRST NUMBER: "))
    b = int(input("INSERT THE SECOND NUMBER: "))

    print("THE RESULT IS", a-b)

    if a > b:
        print("THE RESULT IS", a-b)
    else:
        print("***INVALID NUMBER!***")

def multiply():
    a = int(input("INSERT THE FIRST NUMBER: "))
    b = int(input("INSERT THE SECOND NUMBER: "))

    print("THE RESULT IS", a*b)

def divide():
    a = int(input("INSERT THE FIRST NUMBER: "))
    b = int(input("INSERT THE SECOND NUMBER: "))

    if a % b == 0:
        print("THE RESULT IS", a/b)
    else:
        print("THE RESULT IS", a//b)
        print("AND THE REMAINDER IS", a%b)


def calculator():
    while True:
        option = menu()
    
        if option == 1:
            add()

        elif option == 2:
            substract()

        elif option == 3:
            multiply()

        elif option == 4:
            divide()

        elif option == 0:
            print("CLOSING THE APPLICATION...")
            break
    
calculator()
