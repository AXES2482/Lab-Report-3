class SavingsAccount:

    RATE = 0.02    # Single rate for all accounts

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result = 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        return self.balance

    def getName(self):
        return.name

    def getPin(self):
        return self.pin

    def deposit(self, amount):
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        "Computes, deposits, and returns the interest."
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest