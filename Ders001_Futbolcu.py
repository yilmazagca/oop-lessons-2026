
""" Python'da sınıf (class) isimleri PascalCase 
(diğer adıyla UpperCamelCase) standardına göre yazılır. 
Bu kurala göre, sınıf ismindeki her kelimenin ilk harfi 
büyük yazılır ve kelimeler arasına alt çizgi (_) gibi
işaretler konmaz."""

// Burada Futbolcu adında bir sınıf(class) tanımlıyoruz
class Futbolcu:
    def __init__(self, isim, yas, mevki, guc):
        // __init__ özel bir metodtur (magic / dunder (double underscore) methods
        // sınıftan bir örnek alındığında otomatik tetiklenir Futbolcu.__init__ 'e gerek yoktur.
        // istenirse yukarıda guc=80 gibi bir baslangıc degeri atanabilir
                             
        self.isim = isim
        self.yas = yas
        self.mevki = mevki
        self.guc = guc

    def kos(self):
        print(f"{self.isim} koşuyor.")

    def sut(self, guc):
        print(f"{self.isim} {guc} güçte şut çekti.")

futbolcu1 = Futbolcu("Ahmet", 25, "Forvet", 80)

print(f"Futbolcu {futbolcu1.isim} {futbolcu1.guc} şiddetinde şut çekti.")


    
