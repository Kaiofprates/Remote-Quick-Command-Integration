import requests

from src.integration.TokenProvider import TokenProvider


class PullingResponse:
    """
    Classe para fazer requisições autenticadas à API.
    """

    def __init__(self):
        """
        Inicializa a classe com um TokenProvider para gerenciar tokens de autenticação.
        """
        self.token_provider = TokenProvider()
        self.base_url = "https://genai-code-buddy-api.stackspot.com/v1"

    def create_execution(self, slug, input_data):
        """
        Faz uma requisição POST para criar uma execução com o comando rápido.

        Args:
            slug (str): O identificador do comando rápido.
            input_data (str): Os dados de entrada para a execução.

        Retorna:
            dict: A resposta da API em formato de dicionário.
        """
        url = f"{self.base_url}/quick-commands/create-execution/{slug}"
        querystring = {"slug": slug}
        payload = {"input_data": input_data}
        headers = {
            "Content-Type": "application/json",
        }
        headers.update(self.token_provider.get_token())

        response = requests.post(url, json=payload, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()

    def check_execution_status(self, execution_id):
        """
        Faz uma requisição GET para verificar o status de uma execução.

        Args:
            execution_id (str): O ID da execução.

        Retorna:
            dict: A resposta da API em formato de dicionário.
        """
        url = f"{self.base_url}/quick-commands/callback/{execution_id}"
        headers = {
            "User-Agent": "insomnia/9.2.0",
        }
        headers.update(self.token_provider.get_token())

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
