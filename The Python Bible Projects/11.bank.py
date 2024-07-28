class Account:
    def __init__(self, name, balance, min_balance) -> None:
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds")

    def statement(self):
        print(f'Account Balance: ${self.balance}')

class Current(Account):
    def __init__(self, name, balance) -> None:
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self) -> str:
        return f"{self.name}'s current account balance: {self.balance}" 

class Savings(Account):
    def __init__(self, name, balance) -> None:
        super().__init__(name, balance, min_balance = 0)
    def __str__(self) -> str:
        return f"{self.name}'s current account balance: {self.balance}" 
x = Current('Connor', 500)

x.deposit(400)
x.withdraw(100)
x.statement()
