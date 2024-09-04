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
\n
"""

conta_usuario = "admin"
conta_senha = "admin"
saldo_conta = 0
numero_saques = 0
total_saque = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500


def depositar():
    global saldo_conta
    try:
        valor = float(input("Por favor, digite o valor que deseja inserir: "))
        print(f"Você inseriu o valor: {valor}\n")
        saldo_conta += valor
        iniciar_sistema()

    except ValueError:
        print("Valor inválido! Por favor, insira um número.")
        depositar()


def saque():
    global saldo_conta, numero_saques, LIMITE_VALOR_SAQUE, LIMITE_SAQUES

    if numero_saques < LIMITE_SAQUES:
        try:
            valor = float(
                input(
                    f"O seu limite de saques atual é de {LIMITE_SAQUES - numero_saques}. Por favor, digite o valor que deseja sacar!\nLembre-se que o valor máximo para saque é de {LIMITE_VALOR_SAQUE}:\n"
                )
            )
            if valor <= LIMITE_VALOR_SAQUE:
                if valor <= saldo_conta:
                    print(f"Você sacou {valor} da sua conta! Verifique o extrato!")
                    saldo_conta -= valor
                    numero_saques += 1
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


def extrato():
    global saldo_conta, numero_saques

    print(f"Seu extrato atual é de: {saldo_conta} R$!\n")
    print(f"Você já realizou um total de {numero_saques} operações de saque!\n")
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

    if login_usuario == conta_usuario and senha_usuario == conta_senha:
        print("\nBem-Vindo ao sistema!! É um prazer estar de volta!")
        iniciar_sistema()
    else:
        print("\nUsuário ou senha incorreto, por favor tente novamente!")
        iniciar_tela()


iniciar_tela()