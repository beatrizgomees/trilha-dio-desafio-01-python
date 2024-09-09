import history
class Account:
 
    def __init__(self, number, customer):
            self._withdraw = 0
            self._number = number
            self._agency = "0001"
            self._customer = customer
            self._history = history.History()

    @classmethod
    def new_account(cls, customer, number):
        return cls(number, customer)

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency


    @property
    def customer(self):
        return self._customer


    @property
    def history(self):
        return self._history



    @property
    def balance(self):
        return self._withdraw


    def withdraw(self, value):
        withdraw = self.withdraw
        exceeded_withdraw = value > withdraw

        if exceeded_withdraw:
            print("\n@@@ Operation failed! You don't have enough balance. @@@")

        elif value > 0:
            self._withdraw -= value
            print("\n=== Withdrawal completed successfully! ===")
            return True

        else:
            print("\n@@@ Operation failed! The value entered is invalid. @@@")

        return False

    def deposit(self, value):
        if value > 0:
            self._withdraw += value
            print("\n=== Deposit made successfully! ===")
        else:
            print("\n@@@ Operation failed! The value entered is invalid. @@@")
            return False

        return True


