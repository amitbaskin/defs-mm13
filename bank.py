class BankAccount:

    def __init__(self, name, amt):
        self.name, self.amt = name, amt

    def __str__(self):
        return f'Your account, {self.name}, has {self.amt} dollar{"s" if self.amt != 1 else ""}'


if __name__ == '__main__':
    t1 = BankAccount('Bob', 100)
    print(t1)
