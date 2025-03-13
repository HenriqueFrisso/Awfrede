import requests
import os

# Defina sua chave da OpenRouter API
API_KEY = "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"  # Ou substitua pelo valor diretamente

# URL da API OpenRouter
URL = "https://openrouter.ai/api/v1/chat/completions"

# Dados da requisição
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://yourwebsite.com",  # Substitua pelo seu site ou app
    "X-Title": "Haiku Generator"
}

data = {
    "model": "openai/gpt-3.5-turbo",  # Você pode testar outros modelos
    "messages": [
        {"role": "system", "content": "Você é um poeta especialista em haikus."},
        {"role": "user", "content": "Escreva um haiku sobre inteligência artificial."}
    ]
}

# Fazendo a requisição
response = requests.post(URL, headers=headers, json=data)

# Processando a resposta
if response.status_code == 200:
    haiku = response.json()["choices"][0]["message"]["content"]
    print("Haiku gerado sobre IA:\n")
    print(haiku)
else:
    print("Erro:", response.json())
