class BankAccount:
  def __init__(self, balance, deposit_amount, withdraw_amount, interest=.02):
        self.balance = balance
        self.deposit_amount = deposit_amount
        self.withdraw_amount = withdraw_amount
        self.interest = interest
    def deposit(self): 
        print('deposit')
        if self.deposit_amount < 0: 
            return False
        else: 
            return self.balance = self.deposit_amount + self.balance

    def withdraw(self): 
        print('withdraw')
        if self.withdraw_amount < 0: 
            return False
        else: 
            return self.balance = self.balance - self.withdraw_amount
    def accumulate_interest(self): 
        return self.balance = self.balance * self.interest


class ChildrensAccount():
   def __init__(self, balance, deposit_amount, withdraw_amount, interest=0): 
        super().__init__(balance, deposit_amount, withdraw_amount)
        self.interest = interest
    def accumulate_interest():
        self.balance = self.balance + 10 

class OverdraftAccount():
   def __init__(self, overdraft_penalty):
        self.overdraft_penalty = overdraft_penalty
         

# basic_account = BankAccount()
# basic_account.deposit(600)
# print("Basic account has ${}".format(basic_account.balance))
# basic_account.withdraw(17)
# print("Basic account has ${}".format(basic_account.balance))
# basic_account.accumulate_interest()
# print("Basic account has ${}".format(basic_account.balance))
# print()

# childs_account = ChildrensAccount()
# childs_account.deposit(34)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.withdraw(17)
# print("Child's account has ${}".format(childs_account.balance))
# childs_account.accumulate_interest()
# print("Child's account has ${}".format(childs_account.balance))
# print()

# overdraft_account = OverdraftAccount()
# overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))


