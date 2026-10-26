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
import os
import json


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

    def sozluk_yap(self):
        return {
            "adi": self.adi,
            "soyadi": self.soyadi,
            "tc_kimlik": self.tc_kimlik,
            "dogum_tarihi": self.dogum_tarihi,
            "bolum": self.bolum,
            "okul": self.okul,
            "ogrenci_no": self.ogrenci_no
        }


ogrenci1 = Ogrenci("Ahmet", "Yılmaz", "11111111111", "01.01.2000", "Yönetim Bilişim Sistemleri", "Uygulamalı Bilimler Yüksekokulu", "251700001")

#ogrenci1.bilgileri_goster()

ogrenci_bilgileri = []

def verileri_yukle():
    if os.path.exists("ogrenci_bilgileri.json"):
        with open("ogrenci_bilgileri.json", "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)
            for item in veri:
                ogr = Ogrenci(
                    item["adi"],
                    item["soyadi"],
                    item["tc_kimlik"],
                    item["dogum_tarihi"],
                    item["bolum"],
                    item["okul"],
                    item["ogrenci_no"]
                )
                ogrenci_bilgileri.append(ogr)

            print("Öğrenci bilgileri hafızaya yüklendi.")

    else:
        print("Öğrenci bilgileri dosyası bulunamadı. 'ogrenci_bilgileri.json'")


def verileri_kaydet():
    veri = [ogr.sozluk_yap() for ogr in ogrenci_bilgileri]
    with open("ogrenci_bilgileri.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)
    print("Öğrenci bilgileri dosyaya kaydedildi.")


ogrenci_bilgileri.append(ogrenci1)
# print(f"Öğrenci bilgileri listesine {ogrenci1.adi} {ogrenci1.soyadi} eklendi.")


verileri_kaydet()

verileri_yukle()

for ogr in ogrenci_bilgileri:
    ogr.bilgileri_goster()
