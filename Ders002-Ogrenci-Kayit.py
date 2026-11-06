"""
------- Değişkenler -------
adi
soyadi
tc_kimlik
dogum_tarihi
bolum
okul
ogrenci_no
"""

class Ogrenci:
    def __init__(self, adi, soyadi, tc_kimlik, dogum_tarihi, bolum, okul, ogrenci_no):
        self.adi = adi
        self.soyadi = soyadi
        self.tc_kimlik = tc_kimlik
        self.dogum_tarihi = dogum_tarihi
        self.bolum = bolum
        self.okul = okul
        self.ogrenci_no = ogrenci_no

    def bilgileri_goster(self):
        print(f"Öğrencinin Adı: {self.adi}")
        print(f"Öğrencinin Soyadı: {self.soyadi}")
        print(f"Öğrencinin TC Kimlik Numarası: {self.tc_kimlik}")
        print(f"Öğrencinin Doğum Tarihi: {self.dogum_tarihi}")
        print(f"Öğrencinin Bölümü: {self.bolum}")
        print(f"Öğrencinin Okulu: {self.okul}")
        print(f"Öğrencinin Öğrenci Numarası: {self.ogrenci_no}")


ogrenci1 = Ogrenci("Ahmet", "Yılmaz", "11111111111", "01.01.2000", "Yönetim Bilişim Sistemleri", "Uygulamalı Bilimler Yüksekokulu", "251700001")

