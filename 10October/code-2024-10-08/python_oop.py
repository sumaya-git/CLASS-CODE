

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def debit(self):
        pass

    @property
    @abstractmethod
    def credit(self):
        pass

class sprk(Bank):
    def loan(self):
        print('Loan service available.')

    def debit(self):
        print('Debit service available.')

    @property
    def credit(self):
        print('credit service available.')


bank = sprk()

bank.loan()
bank.debit()
print(bank.credit)








