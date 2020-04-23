import PyQt5.QtWidgets as ayq

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__()

        self.sol = 300
        self.ust = 100
        self.en = 500
        self.boy = 550
        self.title = "Ben son örneğim !"

        self.kodlama()

    def kodlama(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol,self.ust,self.en,self.boy)

        self.label1 = ayq.QLabel("Merhaba ben laybıl :)",self)
        self.label1.move(100,70)
        self.label2 = ayq.QLabel("<h2>Merhaba Ben Label</h2>",self)
        self.label2.move(100,100)

        self.line1 = ayq.QLineEdit("line1",self)
        self.buton1 = ayq.QPushButton("Değiştir",self)
        
        self.line1.move(100,150)
        self.buton1.move(200,150)
        
        
        self.line2 = ayq.QLineEdit("line2",self)
        self.buton2 = ayq.QPushButton("Değiştir",self)

        self.line2.move(100,200)
        self.buton2.move(200,200)

        self.buton1.clicked.connect(self.BuTon1)
        self.buton2.clicked.connect(self.BuTon2)
        self.show()

    def BuTon1(self):
        self.label1.setText(str(self.line1.text()))

    def BuTon2(self):
        self.label2.setText(str(self.line2.text()))

    
    # .text() ile'de içeriğini çekiyoruz
    
    


uyg = ayq.QApplication([" "])
pwn = pencere()
uyg.exec_()