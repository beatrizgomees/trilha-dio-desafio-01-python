import transaction
import account

class Client:
    def _init_(self, address):
        self.address = address
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)
    
    def add_account(self, account):
        self.accounts.append(account)