import PyQt5.QtWidgets as ayq # Default artık
import sys,random

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__()
        
        self.sol = 200
        self.ust = 300
        self.en = 300
        self.boy = 300

        self.title = "uwurgluckoffucial"

        self.kodlama()

    def kodlama(self):
        self.setWindowTitle(self.title) # Pencere başlaığını ayarladık
        self.setGeometry(self.sol,self.ust,self.en,self.boy) # Geometry'i ayarladık

        self.buton = ayq.QPushButton("BUTONA BAS",self) # Butona Bas adlı buton oluşturduk
        self.buton.move(100,100) # Az ortaya ittirelim butonu

        self.buton.clicked.connect(self.fayton) # Butona tıklandığı zaman bir def'i çalıştırmak istediğimiz söyledik
        # ve defi içine yerleştirdik . Tetik mekamizması :)
        # self.fayton() 'u çağırdık .

        
        self.show() # göster gardaşım dedik :)

    def fayton(self):
        self.buton.setDisabled(1) # Butonu devre dışı bıraktık

        rakam = random.randint(1,9999) # random rakam belirttik
        print("Random rakam = "+str(rakam)) # bu rakamı butona basıldıkça terminale print ettik
        #işlemler

        self.buton.setDisabled(0) # Butonu etkinleştirdik 

        # NOT : > time.sleep() 2i kullanısranız istemediğiniz sorunlar çıkacaktır :)

if __name__ == "__main__":
    uygulama = ayq.QApplication(sys.argv)
    penc = pencere()
    uygulama.exec_()
