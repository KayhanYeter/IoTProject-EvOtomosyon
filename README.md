# IoTProject-EvOtomosyon
Kocaeli Üniversitesi Bilişim Sistemleri Mühendisliği 3. Sınıf - Nesnelerin İnterneti dersi projesidir.
KOCAELİ ÜNİVERSİTESİ
TEKNOLOJİ FAKÜLTESİ
 
NESNELERİN İNTERNETİ
AKILLI EV PROJESİ
## HAZIRLAYANLAR
* İREM BENGÜ SOYAKLI
* KAYHAN YETER
* YASEMİN GÖKBERK
* İREM KOCAMIŞ

## ÖĞRETİM GÖREVLİSİ
UĞUR YILDIZ

## Raspbian İşletim Sistemi İndirme;
 
İlk olarak işletim Rasbian’ı indirmek için https://www.raspberrypi.org/downloads/raspbian/ adresini ziyaret ettik. İşletim sistemlerini doğrudan .zip dosyası olarak indirmek için “Download ZIP” seçeneğini kullandık.

## İşletim Sistemini Micro-SD Kart’a Yazdırma
 
Rasbian’ı indirdikten sonra SD karta yazmamız için gerekli olan Win32 Disk Imager Programını indirdik.
 
İndirdiğimiz imaj dosyasını zip içerisinden çıkarttık. Ardından daha önce indirdiğimiz win32diskImager programını açtık. İmaj dosyamızı belirtilen yerden seçtik.
Ardından Write butonuna tıklayıp yazma işlemini başlattık. Yazma işlemini ekranda "Write Succesful." Yazısını görünce tamamladık.

 
## Bağlantılar ve Çalıştırma
 
Yazma işlemini bitirdikten sonra bilgisayardan SD kartı çıkarttık Raspberry Pi 3’e taktık.

## Hareket Sensörü 
Hareket algılama sensörü ile evin girişinde ışık yakma işlemini gerçekleştirdik.Evin içine girildiği anda hareket algılandığında led yanmakta ve 20 sn. boyunca yanık durumda kalmaktadır.Daha sonra off duruma gelmektedir.İşleyişi bu şekildedir.

Kullanılan Malzemeler
* Pır sensörü
* Reed röle 
* Jumper kablo 
* Led


## Serve Motor ile Perde Açma 
 
 
Serve motor ile evin içinde perde açma işlemini gerçekleştirdik.Bunu yaparken ldr ışık şiddetini ölçmeden yararlandık.
Kullanılan Malzemeler
* Ldr 
* Kapasitör
* Serve motor
* Jumper Kablo
* Perde

## Requests Kütüphanesi İle Buluta Veri Gönderme İşlemi
Buluta gönderme işlemi için safaribook kitabından faydalandık ve dweet.io ile buluta gönderme işlemini gerçekleştirdik. Daha sonra sensörleri çalıştırarak verileri alıp almadığımızı kontrol ettik.
 

## Buluta Aktarım İçin Gerekli Kodlar
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
* [Robotistan](www.maker.robotistan.com)
* [Safari Book](www.safaribooksonline.com)
* [Rasperrypi](https://www.raspberrypi.org)
* [Pin Rasperry](pinler.raspi-tr.com)
