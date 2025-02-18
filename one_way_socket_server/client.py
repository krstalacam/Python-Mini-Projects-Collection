import socket

# Sunucu adı manuel girmeye gerek yok, kullanıcıdan alınabilir veya sabit tutulabilir
host = input("Bağlanılacak sunucunun adını girin (boş bırakılırsa otomatik yerel sunucuya bağlanır): ")
if not host:
    host = socket.gethostname()  # Eğer boş bırakılırsa varsayılan olarak kendi bilgisayarına bağlanır

port = 55555

# Socket oluştur ve bağlan
s = socket.socket()
s.connect((host, port))
print(f"{host} ({socket.gethostbyname(host)}) adresine bağlandı...")

while True:
    yanit = s.recv(1024)
    if not yanit:
        print("Bağlantı kapatıldı.")
        s.close()
        break
    print("Gelen mesaj:", yanit.decode("utf-8"))
