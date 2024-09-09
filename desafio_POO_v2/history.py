import datetime

import transaction

class History:
    def __init__(self):
        self._transactions = []

    @property
    def transaction(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transacoes.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )