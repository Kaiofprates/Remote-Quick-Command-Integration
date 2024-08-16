import streamlit as st
import time
from src.integration.PullingResponse import PullingResponse

def main():
    # Custom CSS for light background and orange theme
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #f0f0f5;  /* Light background color */
            padding: 20px;
        }
        .stButton>button {
            background-color: #FF6F00;
            color: white;
            margin-top: 20px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #FF6F00;
            padding: 5px;
        }
        .stTextArea>div>div>textarea {
            border: 2px solid #FF6F00;
            padding: 5px;
        }
        .stProgress>div>div>div>div {
            background-color: #FF6F00;
        }
        .stAlert {
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("API Execution Interface - poc remote quick command")

    # Input fields
    st.header("Configurações da Execução")
    project_name = st.text_input("Nome do Projeto", "testremote")
    input_data = st.text_area("Dados de Entrada", "ola mundo")

    if st.button("Iniciar Execução"):
        api_client = PullingResponse()
        try:
            execution_id = api_client.create_execution(project_name, input_data)
            st.success(f"Execução criada com ID: {execution_id}")
            attempts = 0
            max_attempts = 3

            # Create a progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            while attempts < max_attempts:
                status_response = api_client.check_execution_status(execution_id)
                status = status_response.get("progress", {}).get("status")
                status_text.text(f"Status da execução: {status}")

                if status == "COMPLETED":
                    st.success("Execução completada com sucesso.")
                    result = status_response.get("result", {})
                    st.subheader("Resultado")
                    st.text_area("Result", value=str(result), height=200)

                    break

                attempts += 1
                if attempts < max_attempts:
                    st.info("Aguardando 10 segundos antes da próxima verificação...")
                    # Update the progress bar with a value between 0.0 and 1.0
                    progress_bar.progress(attempts / max_attempts)
                    time.sleep(10)
                else:
                    st.warning("Número máximo de tentativas atingido.")
                    progress_bar.progress(1.0)
        except Exception as e:
            st.error(f"Erro na requisição: {e}")

if __name__ == "__main__":
    main()
