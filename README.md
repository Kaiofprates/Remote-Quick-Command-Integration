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
  - `streamlit`

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
streamlit run app.py
```

# GitAI - Analisador de Diferenças entre Branches

Este projeto utiliza o StackSpot IA para analisar as diferenças entre duas branches de um repositório Git e gerar uma descrição detalhada das mudanças em formato Markdown.

## Pré-requisitos

- Python 3.6 ou superior
- Git instalado e configurado
- Dependências do projeto (instaladas via `pip`)

## Instalação

. Clone o repositório do projeto:

. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows, use: .venv\Scripts\activate
    ```
. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para utilizar o programa, execute o seguinte comando, substituindo `<repo_path>`, `<branch_1>` e `<branch_2>` pelos valores apropriados:

```bash
python gitai.py <repo_path> <branch_1> <branch_2>

```
### exemplo de uso: 

#### passando path e branchs
python gitai.py --repo_path 'C:/Users/Dinopc/Documents/Projetos/Repositorios/java_examples' --branch_1 'origin/main' --branch_2 'test/branch'
#### passando a string do diff diretamente
python gitai.py --diff_string "<diff_string>"

```sh
python gitai.py 'C:/Users/Dinopc/Documents/Projetos/Repositorios/java_examples' 'origin/main' 'test/branch'

Execução criada com ID: 01J5DA4CZV2N3TCZ11G5WQSM89
Status da execução: CREATED
Aguardando 10 segundos antes da próxima verificação...
Status da execução: COMPLETED

# Descrição das Mudanças

## Resumo
Foi realizada uma atualização no arquivo `README.md` na branch de destino. A modificação incluiu a adição de três novas linhas ao final do arquivo. Essas linhas adicionadas contêm apenas quebras de linha e a palavra "teste". Não houve outras alterações no conteúdo existente do arquivo.

## Pontos de Atenção
- A adição da palavra "teste" pode ser um placeholder ou um teste temporário. Verifique se essa alteração é intencional e necessária para o projeto.
- A ausência de uma nova linha ao final do arquivo pode causar problemas de formatação em alguns sistemas de controle de versão ou ferramentas de análise de código.

*Data: 2024-08-16 07:00:14*

*Mensagem gerada a partir do StackSpot IA*

```

#### como alternativa, pode-se criar um arquivo shell para auxilio
```shell
#!/bin/bash

# Capture a saída do comando git diff diretamente em uma variável
diff_string=$(git diff)

# Execute o script gitai.py passando a string do diff como argumento
python gitai.py --diff_string "$diff_string"

```
ou criando um arquivo temporário 

```shell
git diff origin/main test/branch > diff_output.txt
python gitai.py --diff_string "$(cat diff_output.txt)"
```