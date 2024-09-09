import transaction

class CurrentAccount:
     def __init__(self, number, customer, limit=500, withdrawal_limit=3):
        super().__init__(number, customer)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

        def withdraw(self, value):
            number_withdrawals = len(
                [transaction for transaction in self.historico.transaction if transaction["tipo"] == Saque.__name__]
            )

            exceeded_limit = value > self.limit
            exceeded_withdrawals = number_withdrawals >= self.withdrawal_limit

            if exceeded_limit:
                print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

            elif value > 0:
                self._saldo -= value
                print("\n=== Withdrawal completed successfully! ===")
                return True


            else:
                return super().withdraw(value)

            return False

        def __str__(self):
            return f"""\
                Agency:\t{self.agency}
                C/C:\t\t{self.number}
                Holder:\t{self.customer.nome}
            """

