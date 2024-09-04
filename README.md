# Sistema Bancário em Python

Este é um projeto simples de sistema bancário em Python que permite realizar operações básicas como depósito, saque e consulta de extrato. O sistema é executado em linha de comando e simula uma conta bancária com funcionalidades básicas.

## Funcionalidades

- **Depósito:** Permite ao usuário adicionar fundos à conta bancária.
- **Saque:** Permite ao usuário sacar dinheiro da conta, respeitando um limite de valor por saque e um limite de saques diários.
- **Extrato:** Exibe o saldo atual da conta e o número de saques realizados.
- **Login:** Verifica o usuário e a senha antes de permitir o acesso ao sistema.

## Estrutura do Projeto

O código é organizado da seguinte forma:

- **`iniciar_tela()`**: Função principal que exibe a tela de login e verifica as credenciais do usuário.
- **`iniciar_sistema()`**: Função que exibe o menu principal após o login e permite ao usuário selecionar uma das operações disponíveis.
- **`depositar()`**: Função que realiza a operação de depósito, adicionando o valor especificado ao saldo da conta.
- **`saque()`**: Função que realiza a operação de saque, subtraindo o valor especificado do saldo, respeitando os limites de saque.
- **`extrato()`**: Função que exibe o saldo atual e o número de saques realizados.

## Requisitos

- Python 3.10 ou superior

## Como Executar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/SeuUsuario/dio_desafio_SistemaBancario.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd dio_desafio_SistemaBancario
    ```

3. **Execute o script principal:**

    ```bash
    python main.py
    ```

4. **Faça login:**
   - Usuário: `admin`
   - Senha: `admin`

5. **Siga as instruções exibidas na tela para realizar as operações bancárias.**

## Uso

Ao iniciar o sistema e fazer login, você verá o seguinte menu:

Bem-vindo ao sistema Bancário!!!

Olá senhor admin! Por favor, digite a opção de sua escolha:

1 - Depósito
2 - Saque
3 - Extrato
0 - Sair

- **Depósito:** Digite `1` e siga as instruções para adicionar fundos à conta.
- **Saque:** Digite `2` para realizar um saque, respeitando os limites estabelecidos.
- **Extrato:** Digite `3` para visualizar o saldo atual e o número de saques realizados.
- **Sair:** Digite `0` para sair do sistema.

## Limites do Sistema

- **Limite de Saques Diários:** O usuário pode realizar até 3 saques por dia.
- **Valor Máximo por Saque:** O valor máximo permitido para um saque é de R$ 500,00.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações ou dúvidas, entre em contato:

- **Email:** 2005rodrigosilva@gmail.com
- **GitHub:** [RodrigoSilvaPereira](https://github.com/RodrigoSilvaPereira)
