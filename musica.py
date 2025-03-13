import subprocess
import os
import speech_recognition as sr
from ytmusicapi import YTMusic
import pygetwindow as gw
import time

def reconhecer_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga o nome da música...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não entendi, tente novamente.")
        return None
    except sr.RequestError:
        print("Erro na API de reconhecimento.")
        return None

def minimizar_janela():
    time.sleep(5)  # Dá tempo para a janela abrir
    try:
        # Obtém a janela do YouTube Music
        janela = gw.getWindowsWithTitle("YouTube Music")[0]  # Alterei o título para "YouTube Music"
        janela.minimize()  # Minimiza a janela
        print("Janela minimizada.")
    except IndexError:
        print("Janela do YouTube Music não encontrada.")

def abrir_youtube_music_aplicativo(url):
    # Caminho para o executável do Chrome
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    
    # Comando para abrir o PWA do YouTube Music com a URL específica
    subprocess.Popen([chrome_path, "--app=" + url])

def tocar_musica(musica):
    # Inicializa a API do YouTube Music
    ytmusic = YTMusic()

    # Pesquisa a música
    resultado = ytmusic.search(musica, filter="songs")
    
    if resultado:
        # Extrai o ID do vídeo da música
        video_id = resultado[0]['videoId']
        url = f"https://music.youtube.com/watch?v={video_id}"
        
        # Abre o YouTube Music diretamente com a música
        abrir_youtube_music_aplicativo(url)
        print(f"Tocando {musica} no YouTube Music...")

        # Minimiza a janela do YouTube Music
        minimizar_janela()
    else:
        print("Música não encontrada.")

# Fluxo principal
comando = reconhecer_comando()
if comando:
    tocar_musica(comando)
