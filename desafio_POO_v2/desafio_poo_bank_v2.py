import textwrap
import history
import transaction
import account
import deposit
import withdraw
from desafio_POO_v2.current_account import CurrentAccount
from desafio_POO_v2.natural_person import NaturalPerson


def menu():
    menu = """\n ===== MENU =====

    1. Depositar
    2. Sacar
    3. Ver Extrato
    4. Nova conta
    5. Listar contas
    6. Novo usuário
    7. Sair
    """
    return input(textwrap.dedent(menu))



def filter_customer(cpf, customers):
    filter_customer = [customer for customer in customers if customer.cpf == cpf]
    return filter_customer[0] if filter_customer else None

def recover_customer_account(customer):
    if not customer.accounts:
        print("\n@@@ Customer does not have an account! @@@")
        return

    # Exibir as contas disponíveis e permitir que o cliente escolha
    print("Available accounts:")
    for i, account in enumerate(customer.accounts):
        print(f"{i + 1}. {account}")

    # Solicitar a escolha do cliente
    try:
        choice = int(input("Choose an account by number: ")) - 1
        if 0 <= choice < len(customer.accounts):
            return customer.accounts[choice]
        else:
            print("Invalid choice! Returning the first account by default.")
            return customer.accounts[0]
    except ValueError:
        print("Invalid input! Returning the first account by default.")
        return customer.accounts[0]


def deposit(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! @@@")
        return

    value = float(input("Enter the deposit amount: "))
    transaction = deposit.Deposit(value)

    account = recover_customer_account(customer)
    if not account:
        return

    customer.make_transaction(account, transaction)




def withdraw(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! @@@")
        return

    value = float(input("Enter the withdraw amount: "))
    transaction = withdraw.Withdraw(value)


    account = recover_customer_account(customer)
    if not account:
        return

    customer.make_transaction(account, transaction)


def display_extract(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! @@@")
        return

    account = recover_customer_account(customer)
    if not account:
        return

    print("\n================ EXTRACT ================")
    transactions = account.historico.transactions

    extract = ""
    if not transactions:
        extract = "No movements were carried out."
    else:
        for account in transactions:
            extract += f"\n{transaction['type']}:\n\tR$ {transaction['value']:.2f}"

    print(extract)
    print(f"\nBalance:\n\tR$ {account.balance:.2f}")
    print("=========================================")


def create_customer(customers):
    cpf = input("Enter CPF (number only): ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("\n@@@ There is already a customer with this CPF! @@@")
        return

    name = input("Enter full name: ")
    date_birth = input("Enter date of birth (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state acronym): ")

    customer = NaturalPerson(name=name, date_birth=date_birth, cpf=cpf, address=address)

    customers.append(customer)

    print("\n=== Client created successfully! ===")


def create_account(account_number, customers, accounts):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found, account creation flow closed! @@@")
        return

    account = CurrentAccount.new_account(customer=customer, number=account_number)
    accounts.append(account)
    customer.contas.append(account)

    print("\n=== Account created successfully! ===")


def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))


def main():
    customers = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            deposit(customers)

        elif option == "2":
            withdraw (customers)

        elif option == "3":
            display_extract(customers)

        elif option == "4":
            create_customer(customers)

        elif option == "5":
            account_number = len(accounts) + 1
            create_account(account_number, customers, accounts)

        elif option == "6":
            list_accounts(accounts)

        elif option == "7":
            break

        else:
            print("\n@@@ Invalid operation, please select the desired operation again. @@@")


main()