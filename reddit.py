# Reddit ile ilgili fonksiyonları içeren bir dosya

# Gerekli kütüphaneleri içe aktarın
import praw
import pymysql
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Reddit API bilgilerinizi girin
client_id = "client_id"
client_secret = "client_secret"
user_agent = "user_agent"

# MySQL veritabanı bilgilerinizi girin
host = "host"
user = "user"
password = "password"
database = "database"

# İstediğiniz subreddit adını girin
subreddit_name = "subreddit"

# Reddit'e giriş yapmak için bir fonksiyon tanımlayın
def login():
    # Selenium ile bir tarayıcı açın
    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/")

    # Giriş sayfasına tıklayın
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[starts-with(@href, 'https://www.reddit.com/login')]")))
    login_button.click()

    # iframe elementine geçin
    iframe = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.reddit.com/login')]")))

    # Kullanıcı adı ve şifre alanlarını doldurun
    username = driver.find_element(By.XPATH, "//input[@id='loginUsername']")
    username.send_keys("kullanıcı_adın")
    password = driver.find_element(By.XPATH, "//input[@id='loginPassword']")
    password.send_keys("şifren")

    # Giriş butonuna basın
    submit_button = driver.find_element(By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']")
    submit_button.click()

    # Ana sayfaya geri dönün
    driver.switch_to.default_content()

# Veritabanına bağlanmak için bir fonksiyon tanımlayın
def connect_db():
    # MySQL veritabanına bağlanın ve bir cursor oluşturun
    db = pymysql.connect(host=host,
                         user=user,
                         password=password,
                         database=database)
    cursor = db.cursor()
    # Veritabanını ve cursoru döndürün
    return db, cursor

# Veritabanından postları almak için bir fonksiyon tanımlayın
def get_posts():
    # Veritabanına bağlanın ve bir cursor oluşturun
    db, cursor = connect_db()
    # Postları seçmek için SQL sorgusu oluşturun
    sql = "SELECT * FROM posts"
    # SQL sorgusunu çalıştırın ve sonuçları alın
    cursor.execute(sql)
    results = cursor.fetchall()
    # Sonuçları bir liste olarak dönüştürün
    posts = []
    for row in results:
        post = {
            "title": row[0],
            "author": row[1],
            "url": row[2],
            "post_id": row[3]
        }
        posts.append(post)
    # Veritabanını kapatın
    db.close()
    # Listeyi döndürün
    return posts

# Reddit'ten postları çekip veritabanına kaydetmek için bir fonksiyon tanımlayın
def crawl_posts():
    # PRAW ile Reddit API'sine bağlanın ve istediğiniz subreddit'i seçin
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    subreddit = reddit.subreddit(subreddit_name)

    # Veritabanına bağlanın ve bir cursor oluşturun
    db, cursor = connect_db()

    # Subreddit'teki yeni postları alın
    for submission in subreddit.new(limit=25):
        # Postun başlığı, yazarı, url'si ve id'sini alın
        title = submission.title
        author = submission.author.name
        url = submission.url
        post_id = submission.id

        # Veritabanına kaydetmek için SQL sorgusu oluşturun
        sql = f"INSERT INTO posts (title, author, url, post_id) VALUES ('{title}', '{author}', '{url}', '{post_id}')"

        # SQL sorgusunu çalıştırın ve değişiklikleri kaydedin
        cursor.execute(sql)
        db.commit()

    # Veritabanını kapatın
    db.close()

# Reddit'ten postları anlık olarak takip etmek için bir fonksiyon tanımlayın
def stream_posts():
    # PRAW ile Reddit API'sine bağlanın ve istediğiniz subreddit'i seçin
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    subreddit = reddit.subreddit(subreddit_name)

    # Subreddit'teki yeni postları stream ile alın
    for post in subreddit.stream.submissions():
        # Postun başlığı, yazarı, url'si ve id'sini alın
        title = post.title
        author = post.author.name
        url = post.url
        post_id = post.id

        # Post ile ilgili istediğiniz işlemi yapın
        # Örneğin, ekrana yazdırın
        print(f"{title} by {author}: {url} ({post_id})")
