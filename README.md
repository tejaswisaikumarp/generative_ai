Text to SQL LLM Application

url: http://localhost:8501

Agenda:
1. Prompt(English langauge) will be given to LLM (Gemini pro).
2. Gemini pro model will generate a query
3. This query will try to execute and read from SQL Database

Implementation:
1. SQLite -- create a database and insert some records. All of these were done using Puthon programming
2. Create an LLM [Inside this, Create a simple UI using Streamlit]
3. This LLM will communicate with the gemini-pro model an then it will communicate with database to give us the answer.
4. Deployed the application to hugging face.
[https://huggingface.co/spaces/tejaswisaikumar/Text_to_SQL__GenerativeAI]