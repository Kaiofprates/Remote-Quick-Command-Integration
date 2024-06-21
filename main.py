# This is a sample Python script.
import time

from src.integration.PullingResponse import PullingResponse

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == "__main__":
    api_client = PullingResponse()
    try:
        execution_id = api_client.create_execution("testremote", "ola mundo")
        print(f"Execução criada com ID: {execution_id}")

        attempts = 0
        max_attempts = 3
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
