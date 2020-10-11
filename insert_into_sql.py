import pypyodbc

def urunEkle(ad, yazar, yayin, baski, tur):
    baglanti = pypyodbc.connect(
    "Driver = {SQL Server};",
    "Server = sunucu_adi;",
    "Database = veritabani_adi;",
    "Trusted_Connection = True;"
    )
    imlec = baglanti.cursor()
    sql = "INSERT INTO Kitaplar(Ad, Yazar, Yayin, Baski, Tur) VALUES (%s, %s, %s, %s, %s)"
    degerler = (ad, yazar, yayin, baski, tur)
    imlec.execute(sql, degerler)
    try:
        baglanti.commit()
        print(f"{imlec.rowcount} adet kayıt eklendi.")
    except pypyodbc.Error as hata:
        print("Bir hata oluştu: ", hata)
    finally:
        baglanti.close()
        print("Veritabanı bağlantısı kapandı.")
        
def urunleriEkle(liste):
    baglanti = pypyodbc.connect(
    "Driver = {SQL Server};",
    "Server = sunucu_adi;",
    "Database = veritabani_adi;",
    "Trusted_Connection = True;"
    )
    imlec = baglanti.cursor()
    sql = "INSERT INTO Kitaplar(Ad, Yazar, Yayin, Baski, Tur) VALUES (%s, %s, %s, %s, %s)"
    degerler = liste
    imlec.executemany(sql, degerler)
    try:
        baglanti.commit()
        print(f"{imlec.rowcount} adet kayıt eklendi.")
    except pypyodbc.Error as hata:
        print("Bir hata oluştu: ", hata)
    finally:
        baglanti.close()
        print("Veritabanı bağlantısı kapandı.")
        
liste = []
while True:
    ad = input("Kitabın adı: ")
    yazar = input("Kitabın yazarı: ")
    yayin = input("Yayın: ")
    baski = input("Kaçıncı baskı: ")
    tur = input("Kitabın türü: ")
    liste.append((ad, yazar, yayin, baski, tur))
    sonuc = input("Ekleme işlemini sürdürmek istiyor musunuz? (E/H): ")
    if sonuc == "h":
        print("Kayıtlarınız veritabanına aktarılıyor.")
        print(liste)
        urunleriEkle(liste)
        break
        
urunEkle(ad, yazar, yayin, baski, tur)
