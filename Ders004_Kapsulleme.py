"""
Kapsülleme (Encapsulation) kavramı, 
nesne yönelimli programlamada (OOP) bir sınıfın içsel durumunu 
ve davranışlarını gizleyerek, dışarıdan erişimi sınırlamak için 
kullanılan bir tekniktir. Bu, veri bütünlüğünü korumak ve sınıfın 
iç işleyişini kontrol etmek için önemlidir.
"""

class Karakter:
    def __init__(self, isim, can, seviye=1):
        self.isim = isim
        self._can = can
        self.__seviye = seviye

    def can_eksilt(self, miktar):
        self._can -= miktar
        if self._can < 0:
            self._can = 0 # tek alt tire

karakter1 = Karakter("Ahmet", 100)

print(karakter1.isim)
print(karakter1._can)  # Accessing the protected attribute directly

karakter1.can_eksilt(30)
print(karakter1._can)  # Accessing the protected attribute directly

# print(karakter1.__seviye)
print(karakter1._Karakter__seviye) 

""" name magling işlemi yaptı,
 __seviye attribute _Karakter__seviye olarak değiştirildi. 
 Bu yüzden direkt olarak erişilemez. """
