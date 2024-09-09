import transaction
import history
import account
from desafio_POO_v2.Trancsaction import Transaction


class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def registrar(self, account):
        successful_transaction = account.deposit(self.value)

        if successful_transaction:
            account.history.add_transaction(self)