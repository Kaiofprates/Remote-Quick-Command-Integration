# Projeto de API Client
https://ai.stackspot.com/

Este projeto contém um cliente Python para interagir com uma API da stackspot AI,
realizando autenticação via OAuth 2.0 e executando comandos rápidos.
O cliente permite a criação de execuções e a verificação do status das execuções até que sejam completadas ou que o número máximo de tentativas seja atingido.

## Funcionalidades

- Autenticação via OAuth 2.0 utilizando `client_credentials`.
- Criação de execuções de comandos rápidos.
- Verificação periódica do status das execuções.

## Estrutura do Projeto

- `TokenProvider`: Classe responsável por obter e gerenciar o token de acesso.
- `ApiClient`: Classe responsável por fazer as requisições autenticadas à API.
- `main.py`: Script de exemplo para utilização do `ApiClient`.

## Requisitos

- Python 3.7+
- Bibliotecas:
  - `requests`
  - `python-dotenv`

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` com as variáveis de ambiente necessárias:
    ```env
    CLIENT_ID=seu_client_id
    CLIENT_SECRET=seu_client_secret
    TOKEN_URL=https://seu-servidor-de-autenticacao/token
    ```

## Uso

Execute o script de exemplo:
```sh
python main.py
```