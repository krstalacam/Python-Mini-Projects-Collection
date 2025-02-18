import socket

# Bilgisayar adını ve IP adresini al
host = socket.gethostname()
ip_address = socket.gethostbyname(host)
port = 55555

# Socket oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print(f"Sunucu başlatıldı...\nBilgisayar Adı: {host}\nIP Adresi: {ip_address}\nPort: {port}")
print("Bağlantılar bekleniyor...")

while True:  # Sürekli yeni istemciler kabul etsin
    c, addr = s.accept()
    print(f'Yeni istemci bağlandı: {addr}')

    while True:
        try:
            mesaj = input("Mesaj gönder: ")
            c.send(mesaj.encode('utf-8'))
        except (ConnectionResetError, BrokenPipeError):
            print(f"İstemci {addr} bağlantıyı kesti. Yeni istemciler bekleniyor...")
            break  # İç döngüden çık, yeni istemcileri kabul etmeye devam et

    c.close()  # Bağlantıyı kapat, ancak sunucu çalışmaya devam et
