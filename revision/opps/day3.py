# bank
# class level variable - country
# constructor  - fn , ln , accNo transactions
# deposit() , withdrawl()
# static - total accounts
# class level for name change


class Bank:
    country = "India"
    count = 0

    def __init__(self, fn, ln, acc, bal):
        self.firstName = fn
        self.lastName = ln
        self.accNo = acc
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)

    def withdrawl(self, amount):
        if (self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")

    def lastFiveTransaction(self, x):
        return self.transactions[-x::]

    @classmethod
    def changeCountry(cls, cl):
        cls.country = cl

    @staticmethod
    def objCount():
        return Bank.count


A = Bank("Aboli", "wandhare", 123, 1000)
B = Bank("Bilal", "Bilam", 123, 1000)
C = Bank("catty", "parry", 123, 1000)
D = Bank("denis", "dudani", 123, 10000000)
E = Bank("elvish", "yadav", 123, 100000000)

print(Bank.objCount())
A.withdrawl(1000000000)
A.deposit(30000000)
A.deposit(30000)
A.deposit(3000)
A.deposit(30)
