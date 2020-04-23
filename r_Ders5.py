import PyQt5.QtWidgets as ayq

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__()

        self.sol = 100
        self.ust = 100
        self.en = 500
        self.boy = 400

        self.kodlama()

    def kodlama(self):
        self.setGeometry(self.sol,self.ust,self.en,self.boy)

        self.label = ayq.QLabel("<h1>Ben htmlli yazıyım</h1>",self)
        self.label_2 = ayq.QLabel("Ben normal yazıyım",self)
        self.label.move(100,100)
        self.label_2.move(100,135)

        self.buton = ayq.QPushButton("sil",self)
        self.buton.clicked.connect(self.sil)
        self.buton.move(100,160)
        
        self.show()


    def sil(self):
        self.label.clear()
        self.label_2.clear()
        self.buton.setText("Silindi :D")

if __name__ == "__main__":
    uygulama = ayq.QApplication([" "])
    pen = pencere()
    uygulama.exec_()
