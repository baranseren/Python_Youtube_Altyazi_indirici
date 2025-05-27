# YouTube Altyazı İndirici

Bu Python betiği, YouTube videolarından Türkçe veya İngilizce altyazıları indirmenizi sağlayan basit bir masaüstü uygulamasıdır.
İndirilen altyazılar, videonun başlığı ve indirme tarihi ile adlandırılmış bir `.txt` dosyasına kaydedilir.

## Özellikler

* Kullanıcı dostu arayüz (Tkinter ile oluşturulmuştur).
* YouTube video linkinden altyazı indirme imkanı sunar.
* Türkçe ve İngilizce altyazı desteği mevcuttur (öncelik Türkçe altyazıdadır, bulunamazsa İngilizce altyazıyı dener).
* Video başlığını YouTube sayfasından otomatik olarak çeker.
* Dosya adları için video başlığını normalleştirir (Türkçe karakterleri İngilizce eşdeğerlerine dönüştürür, özel karakterleri temizler ve boşlukları alt çizgi ile değiştirir).
* İndirilen altyazıları `YYYYAAGÜN_normalize_edilmis_baslik.txt` formatında (örneğin, `20250527_ornek_video_basligi.txt`) kaydeder.
* İşlem durumu hakkında kullanıcıya bilgi verir (örneğin: "İndirildi: 20250527_ornek_video_basligi.txt").
* Yeni bir link girildiğinde veya yazı yazılmaya başlandığında önceki durum mesajını temizler.

## Gereksinimler

* Python 3.x sürümü.
* `requests` kütüphanesi.
* `beautifulsoup4` kütüphanesi.
* `youtube-transcript-api` kütüphanesi.
* `tkinter` kütüphanesi (Genellikle Python standart kütüphanesi ile birlikte gelir).

## Kurulum

Projeyi kullanmadan önce gerekli Python kütüphanelerini yüklemeniz gerekmektedir.
Aşağıdaki komutu terminal veya komut istemcisinde çalıştırarak kütüphaneleri yükleyebilirsiniz:

```bash
pip install requests beautifulsoup4 youtube-transcript-api
