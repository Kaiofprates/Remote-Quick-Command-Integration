import streamlit as st
import time
from src.integration.PullingResponse import PullingResponse

def main():
    # Custom CSS for orange theme
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #FF6F00;
            color: white;
        }
        .stTextInput>div>div>input {
            border: 2px solid #FF6F00;
        }
        .stTextArea>div>div>textarea {
            border: 2px solid #FF6F00;
        }
        .stProgress>div>div>div>div {
            background-color: #FF6F00;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("API Execution Interface - poc remote quick command")

    # Input fields
    project_name = st.text_input("Project Name", "testremote")
    input_data = st.text_area("Input Data", "ola mundo")

    if st.button("Start Execution"):
        api_client = PullingResponse()
        try:
            execution_id = api_client.create_execution(project_name, input_data)
            #st.write(f"Execução criada com ID: {execution_id}")
            attempts = 0
            max_attempts = 3

            # Create a progress bar
            progress_bar = st.progress(0)

            while attempts < max_attempts:
                status_response = api_client.check_execution_status(execution_id)
                status = status_response.get("progress", {}).get("status")
                st.write(f"Status da execução: {status}")

                if status == "COMPLETED":
                    st.write("Execução completada com sucesso.")
                    result = status_response.get("result", {})

                    # Display result in a text area for editing, copying, and pasting
                    result_text = st.text_area("Result", value=str(result), height=200)
                    break

                attempts += 1
                if attempts < max_attempts:
                    st.write("Aguardando 10 segundos antes da próxima verificação...")
                    # Update the progress bar with a value between 0.0 and 1.0
                    progress_bar.progress(attempts / max_attempts)
                    time.sleep(10)
                else:
                    st.write("Número máximo de tentativas atingido.")
                    progress_bar.progress(1.0)
        except Exception as e:
            st.write(f"Erro na requisição: {e}")

if __name__ == "__main__":
    main()