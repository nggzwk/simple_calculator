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
    
    try:
        choice = int(input("CHOOSE THE METHOD: "))
        return choice
    except ValueError:
        print("***PLEASE USE ONLY VALID OPTIONS***")
        return None


def get_two_numbers():
    try:
        a = int(input("INSERT THE FIRST NUMBER: "))
        b = int(input("INSERT THE SECOND NUMBER: "))
        return a, b
    except ValueError:
        print("***PLEASE USE ONLY VALID INTEGERS")
        return None



def add():
    values = get_two_numbers()
    if values:
        a, b = values
        print("THE RESULT IS", a+b)

def substract():
    values = get_two_numbers()
    if values:
        a, b = values
        result = a - b
        if result < 0:
            print("***NEGATIVE RESULT***")
        print("THE RESULT IS", result)

def multiply():
    values = get_two_numbers()
    if values:
        a, b = values
        print("THE RESULT IS", a*b)

def divide():
    values = get_two_numbers()
    if values:
        a, b = values
        if b == 0:
            print("***CANT DIVIDE BY ZERO***")

        elif a % b == 0:
            print("THE RESULT IS", a/b)

        else:
            print("THE RESULT IS", a//b)
            print("AND THE REMAINDER IS", a%b)

def calculator():
    while True:
        option = menu()
    
        if option is None:
            continue
        elif option == 1:
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
        else:
            print("INVALID OPTION")
    
calculator()