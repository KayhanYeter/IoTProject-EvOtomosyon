# IoTProject-EvOtomosyon
Kocaeli Üniversitesi Bilişim Sistemleri Mühendisliği 3. Sınıf - Nesnelerin İnterneti dersi projesidir.
KOCAELİ ÜNİVERSİTESİ
TEKNOLOJİ FAKÜLTESİ
 
NESNELERİN İNTERNETİ
AKILLI EV PROJESİ
##HAZIRLAYANLAR
İREM BENGÜ SOYAKLI
KAYHAN YETER
YASEMİN GÖKBERK
İREM KOCAMIŞ

##ÖĞRETİM GÖREVLİSİ
UĞUR YILDIZ

1)Raspbian İşletim Sistemi İndirme;
 
İlk olarak işletim Rasbian’ı indirmek için https://www.raspberrypi.org/downloads/raspbian/ adresini ziyaret ettik. İşletim sistemlerini doğrudan .zip dosyası olarak indirmek için “Download ZIP” seçeneğini kullandık.
2)İşletim Sistemini Micro-SD Kart’a Yazdırma
 
Rasbian’ı indirdikten sonra SD karta yazmamız için gerekli olan Win32 Disk Imager Programını indirdik.
 
İndirdiğimiz imaj dosyasını zip içerisinden çıkarttık. Ardından daha önce indirdiğimiz win32diskImager programını açtık. İmaj dosyamızı belirtilen yerden seçtik.
Ardından Write butonuna tıklayıp yazma işlemini başlattık. Yazma işlemini ekranda "Write Succesful." Yazısını görünce tamamladık.

 
3)Bağlantılar ve Çalıştırma
 
Yazma işlemini bitirdikten sonra bilgisayardan SD kartı çıkarttık Raspberry Pi 3’e taktık.

Hareket Sensörü 
Hareket algılama sensörü ile evin girişinde ışık yakma işlemini gerçekleştirdik.Evin içine girildiği anda hareket algılandığında led yanmakta ve 20 sn. boyunca yanık durumda kalmaktadır.Daha sonra off duruma gelmektedir.İşleyişi bu şekildedir.

Kullanılan Malzemeler
1-Pır sensörü
2-Reed röle 
3-Jumper kablo 
4-Led


Serve Motor ile Perde Açma 
 
 
Serve motor ile evin içinde perde açma işlemini gerçekleştirdik.Bunu yaparken ldr ışık şiddetini ölçmeden yararlandık.
Kullanılan Malzemeler
1-Ldr 
2-Kapasitör
3-Serve motor
4-Jumper Kablo
5-Perde

Requests Kütüphanesi İle Buluta Veri Gönderme İşlemi
Buluta gönderme işlemi için safaribook kitabından faydalandık ve dweet.io ile buluta gönderme işlemini gerçekleştirdik. Daha sonra sensörleri çalıştırarak verileri alıp almadığımızı kontrol ettik.
 

Buluta Aktarım İçin Gerekli Kodlar
dweetIO = https://dweet.io/dweet/for/
myName = "Raspberry"

#Send to Cloud, dweet.io
    rqsString = dweetIO+myName+'?'+str(temp)
    print(rqsString)
    rqs = requests.get(rqsString)
    print rqs.status_code
    print rqs.headers
    print rqs.content


Kaynakça
1-www.maker.robotistan.com
2-www.safaribooksonline.com
3-raspberrypi.org
4-pinler.raspi-tr.com
