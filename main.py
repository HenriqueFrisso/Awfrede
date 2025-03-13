import speech_recognition as sr
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def ouvir_comando():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para ruídos do ambiente
        audio = recognizer.listen(source)  # Aguarda a fala
    
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")  # Reconhece a fala em português
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao conectar ao serviço de reconhecimento de voz.")
        return None

if __name__ == "__main__":
    falar("Olá, mundo!")  # Fala "Olá, mundo!"
    
    comando_usuario = ouvir_comando()
    if comando_usuario:
        falar(f"Você disse: {comando_usuario}")
