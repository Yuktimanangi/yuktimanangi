Accounts = {101:1000, 102:2000, 103:1500, 104:3000}

def menu(Accounts,ch):
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Logout")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Your balance is: {Accounts[ch]}")   
            
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            Accounts[ch] += amount
            print(f"Deposited {amount}. New balance is: {Accounts[ch]}")
            
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= Accounts[ch]:
                Accounts[ch] -= amount
                print(f"Withdrew {amount}. New balance is: {Accounts[ch]}")
            else:
                print("Insufficient funds.")
                
        elif choice == 4:
            target_account = int(input("Enter account number to transfer to: "))
            if target_account in Accounts:
                amount = int(input("Enter amount to transfer: "))
                if amount <= Accounts[ch]:
                    Accounts[ch] -= amount
                    Accounts[target_account] += amount
                    print(f"Transferred {amount} to account {target_account}. New balance is: {Accounts[ch]}")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid account number.")
                
        elif choice == 5:
            print("Logging out.")
            break
            
                    
while True:
    print(" -------Bank Management System-------")
    ch = int(input("enter the account number: "))
    if ch in Accounts:
        menu(Accounts,ch)
    elif ch == 0:
        print("Exiting the system.")
        break
    else:   
        print("Invalid account number. Please try again.")