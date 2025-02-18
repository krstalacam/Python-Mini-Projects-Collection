# 📡 Basit Socket Sohbet Uygulaması

Merhaba! 👋 Bu projede, Python'un `socket` modülünü kullanarak temel bir istemci-sunucu (client-server) sohbet uygulaması geliştirdik. Sunucu (`server.py`) yalnızca tek bir istemciyi kabul edebilir ve yalnızca sunucu tarafından mesaj gönderilebilir. İstemci (`client.py`) bu mesajları alıp ekrana yazdırır ancak geri mesaj gönderemez. 💬💻

---
## Dil Seçenekleri 🌍
- [Türkçe (Readme)](readme.tr.md)
- [English (Readme)](readme.md)

## 📂 Dosya Açıklamaları

### 1️⃣ `server.py`
🔹 Bilgisayar adını ve IP adresini alır.
🔹 Belirtilen port üzerinden yalnızca bir istemciyi dinler.
🔹 Bağlanan istemciye mesaj gönderir.
🔹 İstemcinin bağlantısını yönetir.

### 2️⃣ `client.py`
🔹 Sunucuya bağlanır ve gelen mesajları ekrana yazdırır.
🔹 Sunucu mesaj göndermediği sürece beklemede kalır.
🔹 Sunucu bağlantıyı kapatana kadar çalışmaya devam eder.

---

## 🚀 Kurulum ve Kullanım

### 🛠️ Gereksinimler
- Python 3.x

### 🏗️ Kurulum
1. **Sunucuyu Başlat** 🖥️
   ```bash
   python server.py
   ```
   Sunucu çalıştığında IP adresini ve bağlantı portunu ekrana yazdırır. ✨

2. **İstemciyi Çalıştır** 💻
   ```bash
   python client.py
   ```
   İstemci, sunucuya bağlandığında gelen mesajları gösterir. 📩

---

## 📝 Notlar
- Sunucu yalnızca tek bir istemciyi kabul eder.
- İstemci sadece sunucudan gelen mesajları okuyabilir, mesaj gönderemez.
- Sunucu kapatılana kadar bağlantı aktif kalır.
- İstemci bağlantıyı kaybederse program sona erer.

🔧 Hata veya geliştirme önerilerin varsa katkıda bulunmaktan çekinme! 🛠️🤓

---

🚀 **Mutlu kodlamalar!** 🎉