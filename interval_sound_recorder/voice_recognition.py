import threading
import queue
import time
import speech_recognition as sr
import os

r = sr.Recognizer()
save_path = "saved_audio"  # Ses dosyalarını kaydedeceğimiz klasör

# Klasör yoksa oluştur
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Ses kaydının şu an yapılıp yapılmadığını takip eden sayaç
recording_status = []  # Aktif kayıt işlemlerini takip etmek için


def record(results, thread_id, audio_queue, max_duration=5):
    recording_status.append(True)  # Kayıt başladı, listeye True ekle
    with sr.Microphone() as mic:
        try:
            audio = r.listen(mic, timeout=0.4, phrase_time_limit=max_duration)  # Dinleme işlemi
            print(f"Thread-{thread_id}: Ses kaydedildi ve kuyruğa eklendi.")
            audio_queue.put(audio)  # Sonucu kuyrukta depola
        except sr.WaitTimeoutError:
            print(f"Thread-{thread_id}: Wait timeout error.")
        finally:
            recording_status.pop()  # Kayıt bitti, listeden True'yu kaldır


def save_audio(audio, file_name):
    with open(file_name, "wb") as f:
        f.write(audio.get_wav_data())
    print(f"Ses dosyası kaydedildi: {file_name}")


def recognize_speech(audio, results):
    file_name = os.path.join(save_path, f"audio_{int(time.time())}.wav")
    save_audio(audio, file_name)

    try:
        result = r.recognize_google(audio, language="tr-TR")
        print(f"Algılanan Ses: {result}")
        results.append(result)  # Sonuçları ekle
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        print(f"Google API Hatası: {e}")


def process_audio_queue(results, audio_queue):
    while True:
        audio = audio_queue.get()  # Kuyruktan bir eleman al
        if audio:
            threading.Thread(target=recognize_speech, args=(audio, results)).start()
        else:
            print("Dinlemede bir sorun oluştu veya zaman aşımı oldu.")


def monitor_time(results, max_duration=5, listen_interval=4):
    audio_queue = queue.Queue()  # Ses kayıtları için bir kuyruk oluştur

    # Kuyruktaki sesleri işlemek için bir thread başlat
    threading.Thread(target=process_audio_queue, args=(results, audio_queue)).start()

    last_start_time = time.time()  # İlk başlama zamanını kaydet
    recording_thread_active = False  # İlk başta hiçbir kayıt yok

    while True:
        elapsed_time = time.time() - last_start_time

        if len(recording_status) == 0:  # Eğer şu anda kayıt yapılmıyorsa
            print(f"Kayıt yok, yeni kayıt başlatılıyor.")
            threading.Thread(target=record, args=(results, 1, audio_queue, max_duration)).start()
            last_start_time = time.time()  # Sayaç sıfırlanıyor
            recording_thread_active = True
        elif elapsed_time >= listen_interval:  # Eğer belirtilen süre geçtiyse
            print(f"{elapsed_time:.2f} saniye geçti, yeni bir paralel kayıt başlatılıyor.")
            threading.Thread(target=record, args=(results, 2, audio_queue, max_duration)).start()
            last_start_time = time.time()  # Yeni kayıt başladığında sayaç sıfırlanıyor
            recording_thread_active = True

        # Eğer mevcut kayıt işlemi bitmişse ve sayaç sıfırlanmışsa
        if not recording_thread_active and len(recording_status) == 0:
            last_start_time = time.time()  # Sayaç sıfırlanıyor
            recording_thread_active = False

        time.sleep(1)  # Sürekli kontrol etmek yerine 1 saniyelik aralıklarla kontrol et


# Ana işlem devam ederken, başka işlemler yapılabilir.
results = []

# Zaman takip ve kayıt işlemini başlatan thread
threading.Thread(target=monitor_time, args=(results, 5, 4)).start()

# Ana döngü: Sonuçları yazdırmak için
while True:
    print(f"Algılanan Sonuçlar: {results}")
    time.sleep(4)  # 5 saniyede bir kontrol et
