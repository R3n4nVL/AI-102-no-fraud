from flask import Flask, request, jsonify
import requests
import openai

app = Flask(__name__)

# Configuração de chave do Form Recognizer
form_recognizer_subscription_key = "sua_chave_form_recognizer"
form_recognizer_endpoint = "https://<sua_região>.api.cognitive.microsoft.com"

# Configuração de chave do OpenAI
openai.api_key = "sua_chave_openai"

@app.route('/analyze', methods=['POST'])
def analyze_document():
    file = request.files['file']
    file_data = file.read()

    # Análise com Form Recognizer (Extrair dados)
    form_recognizer_url = f"{form_recognizer_endpoint}/formrecognizer/documentModels:analyze?api-version=2023-07-31-preview"
    headers = {'Ocp-Apim-Subscription-Key': form_recognizer_subscription_key, 'Content-Type': 'application/pdf'}

    response = requests.post(form_recognizer_url, headers=headers, data=file_data)

    if response.status_code == 202:
        result = response.json()
        extracted_text = result['analyzeResult']['content']  # Extraindo o texto analisado

        # Análise com OpenAI (Detectando Fraude)
        openai_response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"Analisando o seguinte texto de um documento, identifique qualquer possível fraude ou inconsistências: {extracted_text}",
            max_tokens=200
        )
        analysis = openai_response.choices[0].text.strip()

        return jsonify({'analysis': analysis})

    else:
        return jsonify({'error': 'Erro ao analisar documento'}), 400

if __name__ == '__main__':
    app.run(debug=True)
