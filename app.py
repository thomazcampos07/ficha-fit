import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Inicializando cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Esconde elementos da interface
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Inicializa session_state
if "page" not in st.session_state:
    st.session_state.page = "form"  # form | result
if "resultado" not in st.session_state:
    st.session_state.resultado = ""
if "form_data" not in st.session_state:
    st.session_state.form_data = {}

def reset_form():
    st.session_state.page = "form"
    st.session_state.resultado = ""
    st.session_state.form_data = {}

def gerar_ficha():
    with st.spinner("Gerando ficha personalizada..."):
        # Carregar template
        try:
            with open("prompt.txt", "r", encoding="utf-8") as f:
                template = f.read()
        except FileNotFoundError:
            st.error("Arquivo 'prompt.txt' não encontrado.")
            return

        data = st.session_state.form_data
        prompt = template.format(
            idade=data["idade"],
            sexo=data["sexo"],
            peso=data["peso"],
            altura=data["altura"],
            objetivo=data["objetivo"],
            experiencia=data["experiencia"],
            dias_semana=data["dias_semana"],
            tempo_treino=data["tempo_treino"],
            preferencias=", ".join(data["tipo_treino"]) if data["tipo_treino"] else "Nenhuma",
            foco=", ".join(data["foco"]) if data["foco"] else "Nenhum",
            lesoes=data["lesoes"] if data["lesoes"] else "Nenhuma",
            restricoes=data["restricoes"] if data["restricoes"] else "Nenhuma"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente especialista em academias e saúde física."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200,
                temperature=0.7
            )

            st.session_state.resultado = response.choices[0].message.content.strip()
            st.session_state.page = "result"  # Mudar para tela de resultado
            # O Streamlit irá re-executar o script e renderizar a nova página
            st.rerun()

        except Exception as e:
            st.error(f"Erro ao chamar a API: {e}")


# ------------------ PÁGINA DE FORMULÁRIO ------------------
if st.session_state.page == "form":
    st.title("Ficha de Academia Personalizada 🏋️")
    with st.form("ficha_academia"):
        st.header("Seus dados")
        st.session_state.form_data["idade"] = st.number_input("Idade", min_value=10, max_value=100, step=1)
        st.session_state.form_data["sexo"] = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        st.session_state.form_data["peso"] = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
        st.session_state.form_data["altura"] = st.number_input("Altura (cm)", min_value=120, max_value=220, step=1)

        st.header("Objetivo")
        st.session_state.form_data["objetivo"] = st.selectbox(
            "Qual é o seu objetivo principal?",
            ["Ganho de massa muscular", "Perda de gordura", "Definição muscular", "Condicionamento físico", "Saúde geral"]
        )

        st.header("Experiência")
        st.session_state.form_data["experiencia"] = st.selectbox(
            "Qual é o seu nível de experiência?",
            ["Iniciante (menos de 6 meses)", "Intermediário (6 meses a 2 anos)", "Avançado (mais de 2 anos)"]
        )

        st.header("Disponibilidade")
        st.session_state.form_data["dias_semana"] = st.slider("Quantos dias por semana pode treinar?", 1, 7, 3)
        st.session_state.form_data["tempo_treino"] = st.slider("Quanto tempo disponível por treino (em minutos)?", 20, 120, 60)

        st.header("Preferências")
        st.session_state.form_data["tipo_treino"] = st.multiselect(
            "Prefere quais tipos de treino?",
            ["Máquinas", "Pesos livres", "Misto", "Exercícios aeróbicos"]
        )
        st.session_state.form_data["foco"] = st.multiselect(
            "Quer dar foco extra em algum grupo muscular?",
            ["Pernas", "Braços", "Peito", "Costas", "Ombros", "Abdômen", "Nenhum em específico"]
        )

        st.header("Restrições")
        st.session_state.form_data["lesoes"] = st.text_area("Tem alguma lesão ou limitação física?")
        st.session_state.form_data["restricoes"] = st.text_area("Existe algum exercício que não gosta ou não pode fazer?")

        submitted = st.form_submit_button("Gerar ficha")
        if submitted:
            gerar_ficha()


# ------------------ PÁGINA DE RESULTADO ------------------
if st.session_state.page == "result":
    st.title("🎯 Sua ficha de treino personalizada")
    st.markdown(st.session_state.resultado)
    st.button("Gerar nova ficha", on_click=reset_form)