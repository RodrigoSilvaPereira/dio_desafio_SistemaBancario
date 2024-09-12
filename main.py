from datetime import datetime, timedelta

tela_inicio = """
Bem-vindo ao sistema Bancário!!!
Aqui você poderá acessar informações sobre a sua conta!
Primeiramente, realize o login ou faça o cadastro!
1 - Login
2 - Cadastro
"""

tela_sistema = """
Bem-vindo ao sistema Bancário!!!
Olá senhor(a)! Por favor, digite a opção de sua escolha:
    
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
"""

usuarios = {}  # Dicionário para armazenar contas de usuários

LIMITE_TRANSACOES = 10
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
MASCARA_BR = "%d/%m/%Y"
DATA_HOJE = datetime.now().strftime(MASCARA_BR)
DATA_ESTIMADA = (datetime.now() + timedelta(days=1)).strftime(MASCARA_BR)

def criar_conta(usuario, senha):
    return {
        "usuario": usuario,
        "senha": senha,
        "saldo": 0,
        "numero_saques": 0,
        "total_saque": 0,
        "numero_depositos": 0,
        "total_deposito": 0,
        "total_transacoes": 0,
        "transacoes": {
            "depositos": {
                "data": [],
                "valor": []
            },
            "saques": {
                "data": [],
                "valor": []
            }
        }
    }

def cadastrar():
    usuario = input("Digite o nome de usuário para cadastro: ")
    if usuario in usuarios:
        print("Usuário já cadastrado! Por favor, faça login.")
        iniciar_tela()
    senha = input("Digite a senha: ")
    usuarios[usuario] = criar_conta(usuario, senha)
    print("Usuário cadastrado com sucesso!\nFaça login para acessar sua conta.")
    iniciar_tela()

def depositar(conta):
    if conta["total_transacoes"] < LIMITE_TRANSACOES:
        try:
            valor = float(input("Por favor, digite o valor que deseja inserir: "))
            print(f"Você inseriu o valor: {valor:.2f} no dia {DATA_HOJE}!\n")
            conta["saldo"] += valor
            conta["total_transacoes"] += 1
            conta["numero_depositos"] += 1
            conta["total_deposito"] += valor
            conta["transacoes"]["depositos"]["data"].append(DATA_HOJE)
            conta["transacoes"]["depositos"]["valor"].append(valor)
            iniciar_sistema(conta)
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")
            depositar(conta)
    else:
        print(f'Você já realizou o seu limite de transações! Por favor, aguarde até {DATA_ESTIMADA}')

def saque(conta):
    if conta["total_transacoes"] < LIMITE_TRANSACOES:
        if conta["numero_saques"] < LIMITE_SAQUES:
            try:
                valor = float(
                    input(
                        f"O seu limite de saques atual é de {LIMITE_SAQUES - conta['numero_saques']}. "
                        f"Por favor, digite o valor que deseja sacar (máximo {LIMITE_VALOR_SAQUE}):\n"
                    )
                )
                if valor <= LIMITE_VALOR_SAQUE:
                    if valor <= conta["saldo"]:
                        print(f"Você sacou {valor:.2f} da sua conta no dia {DATA_HOJE}! Verifique o extrato!")
                        conta["saldo"] -= valor
                        conta["numero_saques"] += 1
                        conta["total_saque"] += valor
                        conta["total_transacoes"] += 1
                        conta["transacoes"]["saques"]["data"].append(DATA_HOJE)
                        conta["transacoes"]["saques"]["valor"].append(valor)
                    else:
                        print("Saldo insuficiente!")
                    iniciar_sistema(conta)
                else:
                    print(f"O valor máximo para saque é de {LIMITE_VALOR_SAQUE}")
                    saque(conta)
            except ValueError:
                print("Valor inválido! Por favor, insira um número!")
                saque(conta)
        else:
            print("Você já realizou o seu limite de saques! Por favor, aguarde até amanhã!")
            iniciar_sistema(conta)
    else:
        print(f'Você já realizou o seu limite de transações! Por favor, aguarde até {DATA_ESTIMADA}')

def extrato(conta):
    print(f"Informações da Conta:")
    print(f"Usuário: {conta['usuario']}")
    print(f"Saldo atual: {conta['saldo']:.2f} R$")
    print(f"Saques realizados: {conta['numero_saques']}")
    print(f"Total sacado: {conta['total_saque']:.2f} R$")
    print(f"Depósitos realizados: {conta['numero_depositos']}")
    print(f"Total depositado: {conta['total_deposito']:.2f} R$")
    print(f"Total de transações: {conta['total_transacoes']}\n")

    print("Histórico de Transações:")
    for tipo, detalhes in conta["transacoes"].items():
        print(f"{tipo.capitalize()}:")
        for data, valor in zip(detalhes["data"], detalhes["valor"]):
            print(f"{data}: {valor:.2f} R$")
    
    print("Obrigado por utilizar o sistema!\n")
    iniciar_sistema(conta)

def iniciar_sistema(conta):
    opcao = input(tela_sistema)

    match opcao:
        case "1":
            depositar(conta)
        case "2":
            saque(conta)
        case "3":
            extrato(conta)
        case "0":
            exit()
        case _:
            print("Opção não identificada!")
            iniciar_sistema(conta)

def iniciar_tela():
    print(tela_inicio)
    opcao = input("Digite a sua escolha (1-Login, 2-Cadastro): ")

    if opcao == "1":
        login()
    elif opcao == "2":
        cadastrar()
    else:
        print("Opção inválida!")
        iniciar_tela()

def login():
    login_usuario = input("Digite o login do seu usuário: ")
    senha_usuario = input("Digite a senha do usuário: ")

    if login_usuario in usuarios and senha_usuario == usuarios[login_usuario]["senha"]:
        print("\nBem-Vindo ao sistema!! É um prazer estar de volta!")
        iniciar_sistema(usuarios[login_usuario])
    else:
        print("\nUsuário ou senha incorreto, por favor tente novamente!")
        iniciar_tela()

iniciar_tela()
