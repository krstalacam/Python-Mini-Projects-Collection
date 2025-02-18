from datetime import datetime
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import random
import os
import pygame

r = sr.Recognizer()

def remove_old_audio():
    for file in os.listdir():
        if file.endswith(".mp3") and file.startswith("audio-"):
            try:
                os.remove(file)
                print(f"Eski dosya silindi: {file}")
            except Exception as e:
                print(f"Eski dosya silinirken hata oluştu: {e}")

def record():
    with sr.Microphone() as mic:
        print("Dinliyorum...")
        try:
            # 5 saniye boyunca ses bekler, eğer ses gelmezse timeout hatası verir.
            audio = r.listen(mic, timeout=5, phrase_time_limit=5)
            voicer = r.recognize_google(audio, language='tr')
            return voicer
        except sr.WaitTimeoutError:
            print("Ses gelmedi, tekrar deneyin.")
            return ""
        except sr.UnknownValueError:
            print("Anlayamadım")
            return ""

def response(voicer):
    if 'saat' in voicer:
        speak(datetime.now().strftime('%H:%M:%S'))
    elif 'arama' in voicer:
        speak("neyi arıyorsunuz?")
        search = record()
        while search == "":
            search = record()  # Eğer boşsa tekrar kaydeder.
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
    elif 'video' in voicer:
        speak("video ismini söyler misiniz?")
        search = record()
        while search == "":
            search = record()  # Eğer boşsa tekrar kaydeder.
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
    elif 'kapan' in voicer:
        speak('görüşürüz')
        exit()
    else:
        print("error")
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
    voice = record()
    print(voice)
    if voice == "":
        print("Lütfen tekrar deneyin.")
        continue
    response(voice)