import PyQt5.QtWidgets as ayq

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__()
        self.sol , self.ust ,self.en ,self.boy = 200,300,500,400
        self.title= " TEXT KUTSU"
        self.yazi = input("Yazımız ne olacak gardaşü : ")

        self.kodlama()
    def kodlama(self):
        self.setGeometry(self.sol , self.ust ,self.en ,self.boy)
        self.setWindowTitle(self.title)
        self.buton = ayq.QPushButton("BAS VE YZA",self)
        self.buton.clicked.connect(self.yazi_degis)
        self.buton.setToolTip("Basınca yazı yaz inputa bura yazcaz :)")
        self.buton.move(150,20)
        #self.buton.resize(150,200)
        self.plaintext = ayq.QPlainTextEdit(self)
        self.plaintext.move(150,50)
        self.plaintext.setPlainText("Bu yazıdır")


        self.show()




    def yazi_degis(self):
        self.plaintext.setPlainText(self.yazi)



        


if __name__ == "__main__":
    uygulama = ayq.QApplication([" "])
    penc = pencere()
    uygulama.exec_()
        