# ficha-fit

**Streamlit app that generates personalized workout plans with the OpenAI API.**
The user fills in a form (age, goal, experience, weekly availability, focus
areas, injuries and restrictions), and the app fills a prompt template with
those answers and returns a day-by-day plan with exercises and sets. The UI is
in Portuguese.

- **Stack:** Python, Streamlit, OpenAI API, python-dotenv
- **Run it:** `pip install -r requirements.txt`, put `OPENAI_API_KEY=...` in a
  `.env` file, then `streamlit run app.py`
- **Customize:** the prompt lives in [`prompt.txt`](prompt.txt), separate from
  the code

---

## Sobre

Aplicativo web em **Streamlit** que gera **fichas de treino personalizadas**
com a API da OpenAI. O usuário preenche seus dados, objetivos, experiência e
preferências, e o app cria uma ficha de treino detalhada.

## Funcionalidades

- Formulário interativo para coleta de dados do usuário:
  - Idade, sexo, peso, altura
  - Objetivo principal
  - Nível de experiência
  - Disponibilidade semanal e tempo por treino
  - Preferências de treino e foco em grupos musculares
  - Lesões e restrições
- Chamada à API da OpenAI (`gpt-3.5-turbo`) para gerar a ficha
- Tela de resultado separada do formulário
- Opção de gerar uma nova ficha sem reiniciar o app
- Chave da API fora do código, no `.env`

## Estrutura do projeto

```
ficha-fit/
├── app.py             # Interface Streamlit e chamada à OpenAI
├── prompt.txt         # Template de prompt para a OpenAI
├── requirements.txt   # Dependências
└── .env               # Chave da API OpenAI (não versionado)
```

## Instalação

```bash
git clone https://github.com/thomazcampos07/ficha-fit.git
cd ficha-fit
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-..." > .env
```

## Como rodar

```bash
streamlit run app.py
```

O app abre no navegador com o formulário. Depois de enviar, a ficha aparece
numa nova tela.

## Personalização do prompt

O `prompt.txt` contém o template usado para gerar a ficha. Dá para editar a
linguagem, o detalhamento ou as regras sem mexer no código. As variáveis entre
chaves (`{idade}`, `{objetivo}`, `{lesoes}` etc.) são preenchidas com as
respostas do formulário.

## Licença

[MIT](LICENSE)

## Contato

Desenvolvido por **Thomaz Campos** ·
[LinkedIn](https://www.linkedin.com/in/thomaz-campos) ·
[GitHub](https://github.com/thomazcampos07)
