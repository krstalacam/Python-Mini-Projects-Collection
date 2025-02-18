import time
from datetime import datetime
import pygame
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import random
import os

r = sr.Recognizer()


# Önceki ses dosyasını sil
def remove_old_audio():
    for file in os.listdir():
        if file.endswith(".mp3") and file.startswith("audio-"):
            try:
                os.remove(file)
                print(f"Eski dosya silindi: {file}")
            except Exception as e:
                print(f"Eski dosya silinirken hata oluştu: {e}")


# Sesli komutları kaydet
def record():
    with sr.Microphone() as mic:
        audio = r.listen(mic)
        voicer = ""
        try:
            voicer = r.recognize_google_cloud(audio, language='tr')
        except sr.UnknownValueError:
            return voicer
        return voicer


# Komutlara göre yanıtları işleme
def response(voicer):
    if 'saat' in voicer:
        speak(datetime.now().strftime('%H:%M:%S'))
        url = ''
    elif 'arama' in voicer:
        speak("neyii")
        search = input()
        while search == "":
            search = record()
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
    elif 'video' in voicer:
        search = input()
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        time.sleep(1)
    elif 'kapan' in voicer:
        speak('bay')
        url = ''
    else:
        url = ''
    return url


# Ses dosyasını oynatmak için Pygame
def speak(string):
    # Önceki ses dosyasını sil
    remove_old_audio()

    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)

    # Pygame ile ses dosyasını çal
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    # Müzik çalmayı bitene kadar bekle
    while pygame.mixer.music.get_busy():  # Ses çalmaya devam ederken bekler
        pygame.time.Clock().tick(10)

    # Müzik çalması bittiğinde durdur ve dosyayı sil
    pygame.mixer.music.stop()




speak('heyy')
while True:
    write = input()
    response(write)
