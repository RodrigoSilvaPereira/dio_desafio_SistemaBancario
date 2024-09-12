from datetime import datetime, timedelta

tela_inicio = """
Bem-vindo ao sistema Bancário!!!
Aqui você poderá acessar informações sobre a sua conta!
Primeiramente, realize o login!
"""

tela_sistema = """
Bem-vindo ao sistema Bancário!!!
Olá senhor! Por favor, digite a opção de sua escolha:
    
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
"""

conta = {
    "usuario": "admin",
    "senha": "admin",
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

LIMITE_TRANSACOES = 10
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
MASCARA_BR = "%d/%m/%Y"
DATA_HOJE = datetime.now().strftime(MASCARA_BR)
DATA_ESTIMADA = (datetime.now() + timedelta(days=1)).strftime(MASCARA_BR)

def depositar():
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
            iniciar_sistema()

        except ValueError:
            print("Valor inválido! Por favor, insira um número.")
            depositar()
    else:
        print(f'Você já realizou o seu limite de transações! Por favor, aguarde até {DATA_ESTIMADA}')

def saque():
    if conta["total_transacoes"] < LIMITE_TRANSACOES:
        if conta["numero_saques"] < LIMITE_SAQUES:
            try:
                valor = float(
                    input(
                        f"O seu limite de saques atual é de {LIMITE_SAQUES - conta['numero_saques']}. Por favor, digite o valor que deseja sacar!\nLembre-se que o valor máximo para saque é de {LIMITE_VALOR_SAQUE}:\n"
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
                    iniciar_sistema()
                else:
                    print(f"O valor máximo para saque é de {LIMITE_VALOR_SAQUE}")
                    saque()
            except ValueError:
                print("Valor inválido! Por favor, insira um número!")
                saque()
        else:
            print("Você já realizou o seu limite de saques! Por favor, aguarde até amanhã!")
            iniciar_sistema()
    else:
        print(f'Você já realizou o seu limite de transações! Por favor, aguarde até {DATA_ESTIMADA}')

def extrato():
    print(f"Seu saldo atual é de: {conta['saldo']:.2f} R$!\n")
    print(f"Você já realizou um total de {conta['numero_saques']} operações de saque!\n")
    print(f"Você sacou um total de {conta['total_saque']:.2f} R$!\n")
    print(f"Você realizou de {conta['numero_depositos']} operações de depósito!\n")
    print(f"Você depositou um total de {conta['total_deposito']:.2f} R$!\n")
    print(f"Você realizou um total de {conta['total_transacoes']} transações!\n")
    print(f"Histórico de Extratos: \n")
    
    for tipo, detalhes in conta["transacoes"].items():
        print(f"{tipo.capitalize()}:")
        for data, valor in zip(detalhes["data"], detalhes["valor"]):
            print(f"{data}: {valor:.2f}")
    
    print("Obrigado por utilizar meu sistema!\n")
    iniciar_sistema()

def iniciar_sistema():
    opcao = input(tela_sistema)

    match opcao:
        case "1":
            depositar()
        case "2":
            saque()
        case "3":
            extrato()
        case "0":
            exit()
        case _:
            print("Alternativa não identificada!")
            iniciar_sistema()

def iniciar_tela():
    print(tela_inicio)

    login_usuario = input("Digite o login do seu usuário: ")
    senha_usuario = input("Digite a senha do usuário: ")

    if login_usuario == conta["usuario"] and senha_usuario == conta["senha"]:
        print("\nBem-Vindo ao sistema!! É um prazer estar de volta!")
        iniciar_sistema()
    else:
        print("\nUsuário ou senha incorreto, por favor tente novamente!")
        iniciar_tela()

iniciar_tela()
