from calendar import firstweekday

class BankAcount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money_deposit):
        self.balance = self.balance + money_deposit
        return self.balance
    def withdraw(self, money_withdrawn):
        if money_withdrawn > self.balance:
            print("Sorry, you have insufficient funds, would you like to take overdraft? ")
            respond = input("Please, enter Yes or No ")
            if respond.lower() == "yes":
                self.balance = self.balance - money_withdrawn
                print(f"Your account has enter overdraft, your new balance is {self.balance}")
            else:
                money_withdrawn = 0
                self.balance += money_withdrawn
                print(f"Sorry, Your account balance: {self.balance} is lower than your withdrawal: {money_withdrawn}")
        else:
            self.balance = self.balance - money_withdrawn
            return self.balance
while True:
    initial_balance = 100
    first_account_holder = BankAcount(initial_balance)
    try:
        money_deposit = float(input("How much would you like to deposit? "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if money_deposit < 0:
        print("Sorry, input non-negative value ")
        continue
    elif money_deposit >= 0:
        first_account_holder.balance = first_account_holder.deposit(money_deposit)
        print(f"Your new account balance is {first_account_holder.balance}")



    try:
        money_withdrawn = float(input("How much would you like to withdraw? "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if money_withdrawn < 0:
        print("Sorry, input non-negative value ")
        continue
    else:
        first_account_holder.balance = first_account_holder.withdraw(money_withdrawn)
        print(f"Your new account balance is {first_account_holder.balance}")
        another_transaction = input("would like to perform another transaction? ")
        if another_transaction.lower() == "yes":
            continue
        else:
            break


