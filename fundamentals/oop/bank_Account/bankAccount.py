class BankAccount:
    # don't forget to add some default values for these parameters!
# ============================================================
# init method/ instance attributes
# ============================================================
    def __init__(self, int_rate, default_balance):
        # your code here! (remember, instance attributes go here)
        self.interest = int_rate
        self.balance = default_balance
# ============================================================
# instance method
# ============================================================
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
    # your code here
        print(f"acount balance = {self.balance}")
        return self

    def yield_interest(self):
        # your code here
        self.balance = (self.balance * self.interest) + self.balance
# ============================================================
# class attibute
# ============================================================

a1 = BankAccount(.1399, 0)
a2 = BankAccount(.499, 0)
a1.deposit(500).deposit(100).deposit(120).withdraw(200).withdraw(50).yield_interest()
a2.deposit(600).deposit(200).deposit(20).withdraw(100).yield_interest()
a1.display_account_info()
a2.display_account_info()


