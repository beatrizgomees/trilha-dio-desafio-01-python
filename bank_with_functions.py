from datetime import datetime

# Variáveis globais
saldo = 0.0
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACAO = 500

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Você depositou R$ {valor:.2f}")
    mostrar_saldo()

def sacar(valor):
    global saldo, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("Você atingiu o limite de saques.")
    elif valor > saldo:
        print(f"Você não pode sacar esse valor. Saldo atual: R$ {saldo:.2f}")
    elif valor > LIMITE_TRANSACAO:
        print(f"Você não pode sacar mais do que R$ {LIMITE_TRANSACAO:.2f} por transação.")
    else:
        saldo -= valor
        numero_saques += 1
        print(f"Você sacou R$ {valor:.2f}")
        mostrar_saldo()

def mostrar_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")

def mostrar_extrato(depositos, saques):
    print("\n===== EXTRATO =====")
    print(f"USUÁRIO: ABC")
    print(f"DATA DO EXTRATO: {datetime.now().strftime('%d/%m/%Y')}")
    print(f"DEPÓSITOS: R$ {sum(depositos):.2f}")
    print(f"SAQUES: R$ {sum(saques):.2f}")
    mostrar_saldo()

def menu():
    depositos = []
    saques = []
    
    while True:
        print("\nMENU:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
            continue
        
        if opcao == 1:
            valor = float(input("Informe o valor para depósito: R$ "))
            depositar(valor)
            depositos.append(valor)
        
        elif opcao == 2:
            valor = float(input("Informe o valor para saque: R$ "))
            sacar(valor)
            saques.append(valor)
        
        elif opcao == 3:
            mostrar_extrato(depositos, saques)
        
        elif opcao == 4:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
