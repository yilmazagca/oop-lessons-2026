import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def ana_program():
    app = QApplication(sys.argv)
    
    # UI Yükleyiciyi başlatıyoruz
    loader = QUiLoader()
    
    # Python dosyasının bulunduğu klasörü buluyoruz
    mevcut_klasor = os.path.dirname(__file__)
    ui_yolu = os.path.join(mevcut_klasor, "main.ui") # Tasarım dosyanızın adı farklıysa "tasarim.ui" kısmını değiştirin
    
    # Tasarım dosyasını doğrudan pencere olarak yüklüyorsuz
    pencere = loader.load(ui_yolu)
    .
    if not pencere:
        print("Tasarım dosyası yüklenemedi!")
        return

    # Pencereyi ekranda gösteriyoruz
    pencere.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    ana_program()
