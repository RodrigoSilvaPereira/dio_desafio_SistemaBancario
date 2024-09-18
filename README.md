# Sistema de Gerenciamento Bancário

Este projeto é um sistema de gerenciamento bancário simples implementado em Python. O código fornece funcionalidades básicas para criação de clientes, abertura de contas, depósitos, saques e consulta de extratos.

## Funcionalidades

- **Gerenciamento de Clientes**: Criação de clientes e armazenamento de suas informações.
- **Criação de Contas**: Abertura de contas correntes para clientes.
- **Transações Bancárias**: Realização de depósitos e saques.
- **Extrato Bancário**: Visualização de extratos de contas.
- **Listagem de Contas**: Visualização de contas cadastradas.

## Classes e Funcionalidades

### `ContasIterador`
Um iterador para percorrer e exibir informações de contas.

#### Métodos:
- `__init__(self, contas)`: Inicializa o iterador com uma lista de contas.
- `__iter__(self)`: Retorna o próprio iterador.
- `__next__(self)`: Retorna a próxima conta no formato especificado.

### `Cliente`
Classe base para clientes com informações e contas.

#### Métodos:
- `realizar_transacao(self, conta, transacao)`: Realiza uma transação em uma conta.
- `adicionar_conta(self, conta)`: Adiciona uma conta ao cliente.

### `PessoaFisica(Cliente)`
Classe para clientes pessoas físicas.

#### Métodos:
- `__init__(self, nome, data_nascimento, cpf, endereco)`: Inicializa um cliente pessoa física.

### `Conta(ABC)`
Classe abstrata para contas bancárias.

#### Métodos:
- `sacar(self, valor)`: Realiza um saque.
- `depositar(self, valor)`: Realiza um depósito.

### `ContaCorrente(Conta)`
Classe para contas correntes.

#### Métodos:
- `sacar(self, valor)`: Realiza um saque com limite e controle de saques.

### `Historico`
Armazena e gera relatórios de transações.

#### Métodos:
- `adicionar_transacao(self, transacao)`: Adiciona uma transação ao histórico.
- `gerar_relatorio(self, tipo_transacao=None)`: Gera um relatório das transações.

### `Transacao(ABC)`
Classe abstrata para transações.

#### Métodos:
- `registrar(self, conta)`: Registra a transação em uma conta.

### `Saque(Transacao)`
Classe para transações de saque.

#### Métodos:
- `__init__(self, valor)`: Inicializa a transação de saque.

### `Deposito(Transacao)`
Classe para transações de depósito.

#### Métodos:
- `__init__(self, valor)`: Inicializa a transação de depósito.

## Funções

### `log_transacao(func)`
Decorator para registrar e exibir transações realizadas.

### `menu()`
Exibe o menu principal para o usuário.

### `filtrar_cliente(cpf, clientes)`
Filtra clientes pelo CPF.

### `recuperar_conta_cliente(cliente)`
Recupera a primeira conta de um cliente.

### `depositar(clientes)`
Realiza um depósito para um cliente.

### `sacar(clientes)`
Realiza um saque para um cliente.

### `exibir_extrato(clientes)`
Exibe o extrato de uma conta.

### `criar_cliente(clientes)`
Cria um novo cliente.

### `criar_conta(numero_conta, clientes, contas)`
Cria uma nova conta corrente.

### `listar_contas(contas)`
Lista todas as contas.

### `main()`
Função principal que executa o menu e interage com o usuário.

## Como Executar

1. Clone o repositório.
2. Execute o script com Python 3.

```bash
python main.py
```

## Dependencias
- Python 3.x

## Licença

Esse projeto está sob a licença MIT

Você pode ajustar o conteúdo conforme necessário, adicionando informações sobre o arquivo `LICENSE` ou detalhes específicos sobre como configurar o ambiente de desenvolvimento, se necessário.
