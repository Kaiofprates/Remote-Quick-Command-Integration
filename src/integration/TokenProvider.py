import os
from dotenv import load_dotenv
import requests

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


class TokenProvider:
    """
    Classe para gerenciar e fornecer tokens de acesso OAuth 2.0.
    """

    def __init__(self):
        """
        Inicializa a classe carregando as credenciais do cliente e a URL do servidor de autorização.
        """
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.url = os.getenv('TOKEN_URL')
        self.token = None

    def get_token(self):
        """
        Retorna o token de acesso.

        Retorna:
            dict: Cabeçalho de autorização com o token de acesso.
        """
        if not self.token:
            self.token = self._request_token()
        return self.token

    def _request_token(self):
        """
        Solicita um novo token de acesso.

        Retorna:
            dict: Cabeçalho de autorização com o token de acesso.

        Levanta:
            Exception: Se ocorrer um erro na requisição.
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'client_id': self.client_id,
            'grant_type': 'client_credentials',
            'client_secret': self.client_secret,
        }
        response = requests.post(self.url, headers=headers, data=data)

        if response.status_code == 200:
            access_token = response.json().get('access_token')
            return {"Authorization": f"Bearer {access_token}"}
        elif 400 <= response.status_code < 500:
            raise Exception(f"Client error: {response.status_code} - {response.text}")
        elif response.status_code >= 500:
            raise Exception(f"Server error: {response.status_code} - {response.text}")
        else:
            response.raise_for_status()


# Exemplo de uso
if __name__ == "__main__":
    token_provider = TokenProvider()
    try:
        token_dict = token_provider.get_token()
        print(f"Token obtido: {token_dict}")
    except Exception as e:
        print(f"Erro ao obter token: {e}")
