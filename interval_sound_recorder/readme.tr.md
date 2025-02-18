# 🎧 Ses Tanıma ve Kaydı Sistemi

Merhaba! 👋 Bu proje, Python kullanarak ses kaydetme ve Google Speech Recognition API ile konuşmayı metne çevirme işlemini gerçekleştirir. 🎧💬

## Dil Seçenekleri 🌍
- [Türkçe (Readme)](readme.tr.md)
- [English (Readme)](readme.md)

## 🚀 Özellikler

✅ **Gerçek zamanlı ses kaydı**: Mikrofon ile ses kaydı alır.  
✅ **Paralel kayıt işlemleri**: Birden fazla kayıt işlemine aynı anda yönetir.  
✅ **Google Speech Recognition** ile **Türkçe konuşmaları** metne çevirir. 🇹🇷📝  
✅ **Kesintisiz kayıt**: Yeni kaydın başlamasını, mevcut kayıt bitmeden önce gerçekleştirerek, kelime kaybını önler. ⏳🎧

---

## 📌 Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsin. 🛠️

### 1️⃣ Gerekli Paketleri Kur
Bu projeyi çalıştırmadan önce aşağıdaki Python kütüphanelerini yüklemelisin:

```bash
pip install -r requirements.txt
```

Ve işte bu kadar! 🎉 Bilgisayarının mikrofonu üzerinden sesleri kaydedip, metne çevirmeye başlayabilirsin.

---

## 🛠️ Nasıl Çalışıyor?

1️⃣ **Monitor Thread** ⏳
   - Sürekli olarak sesi dinler ve belirli aralıklarla yeni kayıt başlatır.

2️⃣ **Kaydı Thread'leri** 🎧
   - Ses kaydını başlatır ve belirlenen süre boyunca kayıt yapar.
   - **Süre bitiminden hemen önce yeni bir kayıt başlatılır** böylece konuşmanın son kelimeleri kaybolmaz.

3️⃣ **İşleme Thread'i** 🔄
   - Kaydedilen sesi alır, `.wav` dosyası olarak saklar ve Google Speech Recognition ile metne çevirir.

4️⃣ **Sonuçlar** 📝
   - Algılanan metin, bir listeye eklenir ve sürekli ekrana yazdırılır.


---

## ⚠️ Dikkat Edilmesi Gerekenler

❗ **Mikrofonu değiştirirseniz programı yeniden başlatın.!** 🚫🎤  
❗ **Google API üzerinden çeviri yapıldığı için, internet bağlantısına ihtiyacın var.** 🌍💡  

---

✨ Umarım bu proje işine yarar! Eğer beğendiysen bir ⭐ bırakabilirsin! 😊🚀

