# This is a sample Python script.
import time
from datetime import datetime

from src.integration.PullingResponse import PullingResponse
from src.integration.GitIntegration import GitIntegration

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == "__main__":

    data_hora_atual = datetime.now()

    # Formata a data e hora em uma string legível
    data_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

    repo_path = 'C:/Users/Dinopc/Documents/Projetos/Repositorios/java_examples'

    git_integration = GitIntegration(repo_path)
    api_client = PullingResponse()

    diff_description = git_integration.create_diff_description('origin/main', 'test/branch')

    input_data = (f'Você é um experiente engenheiro de software,'
                  f' escreva uma descrição sobre esse diff entre duas branchs partindo do pressuposto que você é um agente de ia treinado para  escrever '
                  f' resumo de mudanças em formato markdown ( um ponto de atenção, não me retorne o proprio diff em sua resposta! ) '
                  f'ótimo! ao fim do texto adicione a data {data_formatada} e uma mensagem dizendo que foi gerada apartir do Stackspot IA:  {diff_description}')


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
