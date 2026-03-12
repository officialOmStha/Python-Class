Running = True
Acc = 5000
Name = input("Enter your full name: \n")
Payee = ""

while (Running):
    print("\tTransaction Simulation\nPress:")
    print(f"Current Balance: {Acc}")
    choice = int(input("1. To add fund\n2. To transfer\n3. To end\n"))

    if (choice == 1):
        fund = int(input("Enter amount to be added: "))
        Acc += fund
        print(f"Fund added successfully to {Name}'s account.")
        print(f"Current Balance: {Acc}")
    elif (choice == 2):
        transTO= input("Enter name of receiver: \n")
        Payee = transTO
        transAmt = int(input("Enter amount to be transfered: "))
        if (transAmt <= Acc):
            Acc -= transAmt
            print(f"Rs. {transAmt} transfered to {Payee}")
            print(f"Current Balance: {Acc}")
        else:
            print("!!! Insufficient Balance !!!\nPlease add enough fund before iniciating transaction.")
            print(f"Current Balance {Acc}")
    
    elif (choice == 3):
        Running = False
    else:
        print("Enter correct choice!!!")
            



