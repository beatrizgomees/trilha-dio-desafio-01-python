import account
from desafio_POO_v2.Trancsaction import Transaction


class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        successful_transaction = account.withdraw(self.value)

        if successful_transaction:
            account.history.add_transaction(self)
