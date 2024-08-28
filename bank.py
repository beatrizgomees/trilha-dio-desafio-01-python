
saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(deposito):
    global saldo
    saldo += deposito
    print(f"você depositou {deposito}")
    print("Saldo: R$ {:.2f}".format(saldo))

def sacar(saque):
    global saldo, numero_saques
    if (saldo >= saque and numero_saques < LIMITE_SAQUES) and saque <= limite:
        saldo -= saque
        print(f"Você sacou {saque}!!")
        print("Saldo: R$ {:.2f}".format(saldo))
        numero_saques += 1

    elif saldo > limite:
        print("Você não pode sacar esse valor. Seu Limite é de 500 reais por transação!")

    elif saque > saldo:
        print("Você não pode sacar esse valor. É maior que seu saldo atual. Saldo: R$ {:.2f}".format(saldo))


    elif numero_saques >= LIMITE_SAQUES:
        print("Você não pode sacar no momenot. Você já utilizou todo o seu Limite de saques")

    else:
        print("Operação falhou! O valor informado é inválido")

def extrato(deposito, saque, saldo):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("""
    ===== EXTRATO =====
    USUÁRIO: ABC
    DATA DO EXTRATO: 25/08/2024
    """)

    print("DEPOSITO: R$ {:.2f}".format(deposito))
    print("SAQUE: R$ {:.2f}".format(saque))
    print("SALDO ATUAL: R$ {:.2f}".format(saldo))




def menu():
    global deposito, saque
    while True:
        print("\nMENU:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        opcao = int(input(menu))

        if opcao == 1:
            print("Depositar")
            deposito = float(input("Informe um valor: ", ))
            depositar(deposito)

        elif opcao == 2:
            print("Sacar")
            saque = float(input("Informe um valor: ", ))
            sacar(saque)

        elif opcao == 3:
            print("Extrato")
            extrato(deposito, saque, saldo)

        elif opcao == 4:
            print("Sair")
            break

        else:
            print("Operacao Inválida, por favor selecione novamente a operação desejada")



menu()