import openai

openai.api_key = "sua_chave_openai"

document_text = "Aqui está o texto extraído do documento analisado."

response = openai.Completion.create(
  engine="gpt-4",  
  prompt=f"Analisando o seguinte texto de um documento, identifique qualquer possível fraude ou inconsistências: {document_text}",
  max_tokens=200
)

print(response.choices[0].text.strip())
