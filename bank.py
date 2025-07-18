def deposit(Accounts, ch, amount):
    if amount > 0:
        Accounts[ch] += amount
        print("dep successfully", Accounts[ch])
    else:
        print("invalid dep amount")

def menu(Accounts, ch):
    while True:
        print("\nWelcome to Account number {}".format(ch))  # Show welcome each time
        print("1.Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Transfer")
        print("5.Logout")
        d = int(input("Enter your choice: "))

        if d == 1:
            print("balance", Accounts[ch])

        elif d == 2:
            amt = int(input("Enter amount to be deposited: "))
            deposit(Accounts, ch, amt)  # Fixed parameter order

        elif d == 3:
            wh = int(input("Enter amount to be withdrawn: "))
            if wh > Accounts[ch]:  # Fixed wrong variable
                print("Insufficient balance")
            else:
                Accounts[ch] -= wh
                print("Amount withdrawn successfully")

        elif d == 4:
            to_acc = int(input("Enter account number to transfer to: "))  # Fixed prompt
            if to_acc not in Accounts:
                print("Invalid account number")
            else:
                amt = int(input("Enter amount to be transferred: "))
                if amt > Accounts[ch]:
                    print("Insufficient balance")
                else:
                    Accounts[ch] -= amt
                    Accounts[to_acc] += amt
                    print("Transfer successful")

        elif d == 5:
            print("Logging out")
            break

        else:
            print("Invalid choice")


Accounts = {101: 1000, 102: 1000, 103: 1000}

while True:
    ch = int(input("Enter your account number (or 0 to exit): "))
    if ch in Accounts:
        print("\nWelcome to Account number {}".format(ch))  # STARTS HERE
        menu(Accounts, ch)
        print("Account Balance", Accounts[ch])
    elif ch == 0:
        print("Exit")
        break
    else:
        print("Invalid Account number")
