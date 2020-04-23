import PyQt5.QtWidgets as ayq # default import etme şeklimiz
import sys

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__() # QWidget 'ın yetkilerini arakladık
        self.sol = 200 
        self.ust = 300
        self.en = 300
        self.boy = 400
        
        self.title = "But On Sj"

        self.kodlar() # kodlar elemanını çağırdık

    def kodlar(self):
        self.setWindowTitle(self.title) # title'ı çektik
        self.setGeometry(self.sol , self.ust , self.en , self.boy)      # geometry'ı çektik
        
        self.buton = ayq.QPushButton("Ben Butonum",self) # Buton değerini verdik , butonun  gerçekten buton olduğunu kanıtladık , sonradan da ben butonum dedirttik . Sonradan büyük abisi self'i davet ettik
        
        self.buton.setToolTip("ben butonun açıklamasıyım :)") # Butonun ne iş gördüğünü belirten elemanı butona hediye ettik

        #self.buton.resize(100,50) # | Butonumuzu büyütüp küçültebiliriz ama gerek yok :) | Tabiki dene !
        
        #self.buton.setDisabled(1) # | Butonu devre dışı bırakabiliyoruz [ :) ] İleride lazım olacak | Tabiki dene ! (1 bool değeri !)

        self.buton.move(20,30) # küçük butonumuzu x,y konumunda 20,30'a taşıdık

        self.show() # Elemanları görünür yaptık 

if __name__ == "__main__":
    uygulama = ayq.QApplication(sys.argv) # Muhtemelen sys.argv ile birtakım ince ayarlar yapabiliyor kullanıcılar (PyQt uygulamalara) o yüzden ellemeye gerek yok
    pancar = pencere()
    uygulama.exec_()
    print("Görünüüşe göre butonlu uygulamamızı kapadın .. ")

    # Diğer betiğe ...
