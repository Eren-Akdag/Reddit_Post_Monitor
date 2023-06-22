# Reddit Crawler

Bu proje, Reddit'ten belirli bir subreddit'in postlarını çekip, MySQL veritabanına kaydeden ve Flask ile API olarak servis eden bir uygulamadır. Ayrıca, Reddit'ten postları anlık olarak takip edebilen ve kodunu Docker ile çalıştırabilen bir uygulamadır.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki gereksinimleri karşılamanız gerekmektedir:

- Python 3.9 veya üstü
- PRAW kütüphanesi
- PyMySQL kütüphanesi
- Selenium kütüphanesi
- Flask kütüphanesi
- Pytest kütüphanesi
- Docker
- ChromeDriver
- MySQL veritabanı
- Reddit hesabı ve API bilgileri

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Bu repoyu klonlayın veya indirin.
2. Proje klasörüne girin.
3. requirements.txt dosyasındaki gerekli kütüphaneleri pip ile yükleyin.
4. MySQL veritabanında posts adında bir tablo oluşturun. Tablonun title, author, url ve post_id adında dört sütunu olmalıdır.
5. reddit.py dosyasında Reddit API bilgilerinizi ve MySQL veritabanı bilgilerinizi girin. Ayrıca istediğiniz subreddit adını da girin.
6. Dockerfile dosyasını kullanarak bir Docker imajı oluşturun.
7. Oluşturduğunuz Docker imajını çalıştırın.

## Kullanım

Bu projeyi çalıştırdığınızda, aşağıdaki işlemleri yapabilirsiniz:

- Reddit'e giriş yapmak için login fonksiyonunu çağırın.
- Veritabanından postları almak için get_posts fonksiyonunu çağırın.
- Reddit'ten postları çekip veritabanına kaydetmek için crawl_posts fonksiyonunu çağırın.
- Reddit'ten postları anlık olarak takip etmek için stream_posts fonksiyonunu çağırın.
- Flask ile API oluşturmak için api.py dosyasını flask ile çalıştırın. API rotası /api/posts şeklindedir.
- Pytest ile test yazmak için test_reddit.py dosyasını pytest ile çalıştırın.

## İletişim

Bu proje hakkında herhangi bir soru veya öneriniz varsa, lütfen benimle iletişime geçin. E-posta adresim: meakdaggg@gmail.com

