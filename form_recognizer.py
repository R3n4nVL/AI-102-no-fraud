import requests

subscription_key = 'sua_chave_de_assinatura'
endpoint = 'https://<sua_região>.api.cognitive.microsoft.com'
form_recognizer_url = f'{endpoint}/formrecognizer/documentModels:analyze?api-version=2023-07-31-preview'

headers = {
    'Content-Type': 'application/pdf',  # Supondo que você está enviando um arquivo PDF
    'Ocp-Apim-Subscription-Key': subscription_key,
}

with open("documento.pdf", "rb") as f:
    data = f.read()

response = requests.post(form_recognizer_url, headers=headers, data=data)

if response.status_code == 202:
    result = response.json()
    print(result)
else:
    print("Erro:", response.status_code, response.text)
