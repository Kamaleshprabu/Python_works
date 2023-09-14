class bankaccount:
    def __init__(self,account_number,account_holder_name,initial_balance=0.0):
        self.__account_number=account_number
        self.__account_holder_name=account_holder_name
        self.__account_balance=initial_balance

    def desposit(self,amount):
        if amount>0:
            self.__account_balance+=amount
            print("desposited ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
        else:
          print("invaild deposit amount.")

    def withdraw(self,amount):
      if amount>0 and amount<=self.__account_balance:
        self.__account_balance-=amount
        print("withdrew ₹{}. new balance: ₹{}".format(amount,self.__account_balance))
      else:
        print("invaild withdrawal amount or insufficient balance.")

    def display_balance(self):
        print("account balance for {} (account #{}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))

account=bankaccount(account_number="111222333",
                    account_holder_name="rajesh",
                    initial_balance=4000.0)

account.display_balance()
account.desposit(500.0)
account.withdraw(500.0)
account.display_balance()
