from typing import Literal

# Initial balance
balance: Literal[1000] = 1000

def check_balance():
    """Func tion to check the current balance."""
    print("Your Current Balance is:", balance, "Rupees only")

def money_withdrawal(amount: int):
    """Function to withdraw money from the account."""
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: {balance} Rupees")

def money_deposit(amount: int):
    """Function to deposit money into the account."""
    global balance
    balance += amount
    print(f"Deposit successful. New balance: {balance} Rupees")

def main():
    """Main function to handle user input and execute appropriate actions."""
    pin = input("Enter Your Pin: ")
    if pin == "1234":
        print("Enter 1 for Balance Inquiry")
        print("Enter 2 for Money Withdrawal")
        print("Enter 3 for Money Deposit")
        option = input("Select an option (1/2/3): ")

        if option == "1":
            check_balance()
        elif option == "2":
            amount = int(input("Enter amount to withdraw: "))
            money_withdrawal(amount)
        elif option == "3":
            amount = int(input("Enter amount to deposit: "))
            money_deposit(amount)
        else:
            print("Invalid option selected")
    else:
        print("Invalid Pin")

if __name__ == "__main__":
    main()
