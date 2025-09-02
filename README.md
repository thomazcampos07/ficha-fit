# ficha-fit

Este projeto é um aplicativo web interativo desenvolvido com **Streamlit** que gera **fichas de treino personalizadas** usando a API da OpenAI. O usuário preenche seus dados, objetivos, experiência e preferências, e o app cria uma ficha de treino detalhada e personalizada.

---

## Funcionalidades

- Formulário interativo para coleta de dados do usuário:
    - Idade, sexo, peso, altura
    - Objetivo principal
    - Nível de experiência
    - Disponibilidade semanal e tempo por treino
    - Preferências de treino e foco em grupos musculares
    - Lesões e restrições
    - Chamada à API da OpenAI (gpt-3.5-turbo) para gerar a ficha personalizada
    - Tela de resultado separada do formulário
    - Opção de gerar uma nova ficha sem reiniciar o app
    - Armazenamento seguro de chaves da API usando `.env`

---

## Estrutura do projeto

ficha-fit/
├── app.py             # Script principal do Streamlit  
├── prompt.txt         # Template de prompt para a OpenAI  
├── .env               # Chave da API OpenAI (não versionar)  
├── requirements.txt   # Dependências do projeto  
└── README.md          # Este arquivo  

---

## Instalação

1. Clone o repositório:  
   `git clone https://github.com/seu-usuario/ficha-fit.git`  
   `cd ficha-fit`

2. Crie um ambiente virtual (opcional, mas recomendado):  
   `python -m venv .venv`  
   Linux/Mac: `source .venv/bin/activate`  
   Windows: `.venv\Scripts\activate`

3. Instale as dependências:  
   `pip install -r requirements.txt`

4. Configure sua chave da OpenAI no arquivo `.env`:  
   `OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXX`

> ⚠️ Nunca compartilhe sua API Key publicamente.

---

## Como rodar

Execute o app com:  
`streamlit run app.py`  

O aplicativo abrirá em seu navegador padrão, mostrando o formulário para preenchimento. Após enviar, será exibida a ficha de treino em uma nova tela.

---

## Dependências

- streamlit  
- openai  
- python-dotenv  

---

## Personalização do prompt

O arquivo `prompt.txt` contém o template do prompt usado para gerar a ficha de treino. Você pode editar este arquivo para ajustar a linguagem, o detalhamento ou as regras de criação da ficha.

Exemplo de conteúdo do `prompt.txt`:

Você é um treinador especialista. Crie uma ficha de treino detalhada para o seguinte usuário:

Idade: {idade}  
Sexo: {sexo}  
Peso: {peso}  
Altura: {altura}  
Objetivo: {objetivo}  
Experiência: {experiencia}  
Dias por semana: {dias_semana}  
Tempo por treino: {tempo_treino} minutos  
Preferências: {preferencias}  
Foco extra: {foco}  
Lesões/limitações: {lesoes}  
Restrições: {restricoes}  

Responda de forma clara e organizada, detalhando os exercícios por dia e séries recomendadas.

---

## Licença

Este projeto é open-source e pode ser usado livremente para fins educacionais ou pessoais.

---

## Contato

Desenvolvido por **Thomaz Campos**  
[GitHub](https://github.com/seu-usuario) | [Email](mailto:seu-email@exemplo.com)
