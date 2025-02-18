# 🤖 Sesli Asistan README

Merhaba! 👋 Bu proje, Python kullanarak sesli komutlarla çalışan basit bir asistan oluşturmanıza yardımcı olur. 🎙️💡 Sesli komutları algılar, Google'da arama yapar, saati söyler ve hatta kapanabilir. 🚀

## Dil Seçenekleri 🌍
- [Türkçe (Readme)](readme.tr.md)
- [English (Readme)](readme.md)

## 📌 Özellikler
- 🎤 **Sesli komutları algılar** (Google Speech Recognition kullanır)
- 🕰️ **Saati söyleyebilir**
- 🔍 **Google'da arama yapabilir**
- 📺 **YouTube'da video arayabilir**
- 🎵 **Metni sese çevirip sesli yanıt verir** (gTTS ve pygame ile)
- 🗑️ **Eski ses dosyalarını temizler**
- ⏳ **Zaman aşımı kontrolü ile bekleme süresini yönetir**

## 🚀 Kurulum
Projeyi kullanabilmek için aşağıdaki kütüphaneleri yüklemeniz gerekiyor:
```sh
pip install -r requirements.txt
```
Ek olarak, bilgisayarınızda **pygame** için gerekli ses sürücülerinin yüklü olduğundan emin olun. 🎧

## 🔥 Kullanım
### Programı Çalıştırma
Projede iki farklı çalışma yöntemi bulunmaktadır:

1️⃣ **Sesli Kontrol ile Çalıştırma:**
```sh
python by_voice_control.py
```
Bu yöntemle program doğrudan mikrofon üzerinden sesli komutları dinler ve verilen talimatlara göre işlem yapar. 🎙️

2️⃣ **Metinle Kontrol ile Çalıştırma:**
```sh
python by_text_control.py
```
Bu yöntemde sesli komut yerine, yazılı komutlar girerek asistanı kontrol edebilirsiniz. Klavyeden giriş yaparak komutları çalıştırabilirsiniz. ⌨️

### Kullanılabilecek Komutlar
- **"Saat kaç?"** ⏰ (Saati söyler)
- **"Arama yap --> Python"** 🔍 (Google'da "Python" kelimesiyle arama yapar)
- **"Video aç --> Lo-fi müzik"** 📺 (Belirtilen kelimeyle YouTube'da arama yapar)
- **"Kapan"** 👋 (Programı sonlandırır)

## 🛠️ Nasıl Çalışıyor?
- `record()` fonksiyonu mikrofonu dinler ve sesi metne çevirir.
- `response()` fonksiyonu kullanıcının söylediğini analiz eder ve yanıt üretir.
- `speak()` fonksiyonu yanıtı sesli olarak oynatır.
- `remove_old_audio()` eski ses dosyalarını temizler.

## ⚠️ Dikkat Edilmesi Gerekenler
- **İnternet bağlantınızın olması gerekiyor** çünkü Google Speech Recognition ve gTTS çevrimiçi çalışıyor. 🌐
- **Arka planda mikrofon erişiminin açık olduğundan emin olun!** 🎤
- Eğer ses tanıma çalışmazsa, `print(voice)` satırını kontrol ederek asistanın ne algıladığını görebilirsiniz. 🧐

🚀 **Eğlenceli kodlamalar!** 🧑‍💻💖

