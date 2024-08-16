import argparse
import subprocess
import time
from datetime import datetime

from src.integration.GitIntegration import GitIntegration
from src.integration.PullingResponse import PullingResponse

class GitAI:
    def __init__(self, repo_path=None):
        self.repo_path = repo_path

    def create_diff_description(self, branch_1: str, branch_2: str) -> str:
        try:
            # Navega até o diretório do repositório
            result = subprocess.run(
                ['git', 'diff', branch_1, branch_2],
                cwd=self.repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode != 0:
                raise Exception(f"Error executing git diff: {result.stderr}")
            return result.stdout
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    # Configura o argparse para capturar os argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Process some branches or a diff string.')
    parser.add_argument('--repo_path', type=str, help='Caminho do repositório')
    parser.add_argument('--branch_1', type=str, help='Nome da primeira branch')
    parser.add_argument('--branch_2', type=str, help='Nome da segunda branch')
    parser.add_argument('--diff_string', type=str, help='String contendo o diff')

    args = parser.parse_args()

    data_hora_atual = datetime.now()
    data_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

    api_client = PullingResponse()

    if args.diff_string:
        diff_description = args.diff_string
    else:
        if not args.repo_path or not args.branch_1 or not args.branch_2:
            raise ValueError("repo_path, branch_1, and branch_2 must be provided if diff_string is not used.")
        git_integration = GitIntegration(args.repo_path)
        diff_description = git_integration.create_diff_description(args.branch_1, args.branch_2)

    input_data = (f'Você é um experiente engenheiro de software,'
                  f' escreva uma descrição sobre esse diff entre duas branchs partindo do pressuposto que você é um agente de ia treinado para escrever '
                  f' resumo de mudanças em formato markdown ( um ponto de atenção, não me retorne o proprio diff em sua resposta! ) '
                  f'ótimo! ao fim do texto adicione a data {data_formatada} e uma mensagem dizendo que foi gerada apartir do Stackspot IA: {diff_description}')

    try:
        execution_id = api_client.create_execution("testremote", input_data)
        print(f"Execução criada com ID: {execution_id}")

        attempts = 0
        max_attempts = 5
        while attempts < max_attempts:
            status_response = api_client.check_execution_status(execution_id)
            status = status_response.get("progress", {}).get("status")

            print(f"Status da execução: {status}")

            if status == "COMPLETED":
                print(status_response.get("result", {}))
                print("Execução completada com sucesso.")
                break

            attempts += 1
            if attempts < max_attempts:
                print("Aguardando 10 segundos antes da próxima verificação...")
                time.sleep(10)
        else:
            print("Número máximo de tentativas atingido.")
    except Exception as e:
        print(f"Erro na requisição: {e}")