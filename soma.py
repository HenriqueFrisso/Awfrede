import requests
import speech_recognition as sr
import pyttsx3

# Substitua pela sua chave da OpenRouter API
API_KEY = "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"

# URL da API OpenRouter
URL = "https://openrouter.ai/api/v1/chat/completions"

# Configuração dos headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://yourwebsite.com",  # Substitua pelo seu site ou app
    "X-Title": "Pesquisa por Voz"
}

# Função para falar o texto
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Função para capturar áudio do microfone e converter em texto
def ouvir_comando():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para ruído ambiente
        audio = recognizer.listen(source)  # Captura o áudio

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")  # Converte para texto
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao conectar ao serviço de reconhecimento de voz.")
        return None

# Função para fazer a requisição à IA
def pesquisar_ia(pergunta):
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Você é um assistente que responde perguntas de forma clara e objetiva."},
            {"role": "user", "content": pergunta}
        ]
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        resposta = response.json()["choices"][0]["message"]["content"]
        print("\nResposta da IA:")
        print(resposta)
        return resposta
    else:
        print("Erro ao acessar IA:", response.json())
        return "Não consegui obter uma resposta."

# Executando o programa
if __name__ == "__main__":
    falar("Olá! O que você quer saber?")
    
    comando_usuario = ouvir_comando()
    if comando_usuario:
        resposta_ia = pesquisar_ia(comando_usuario)
        falar(resposta_ia)
