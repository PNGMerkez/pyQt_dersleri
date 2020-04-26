import PyQt5.QtWidgets as ayq # Default
import sys,os,platform
import webbrowser

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__()
        self.sol , self.ust ,self.en ,self.boy = 200,300,500,400
        self.title= " TEXT KUTSU"

        self.kodlama()

    def kodlama(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol , self.ust ,self.en ,self.boy)

        self.cikis = ayq.QMessageBox.question(self,"?","Çıkmak istiyor musun ? ",ayq.QMessageBox.Yes | ayq.QMessageBox.No, ayq.QMessageBox.No)
        if self.cikis == ayq.QMessageBox.Yes :
            sys.exit()

        self.buton = ayq.QPushButton("BEN BUTONUM",self)
        self.plain = ayq.QPlainTextEdit(self)
        self.line = ayq.QLineEdit(self)
        self.line.setText(str(platform.uname()))


        self.buton.clicked.connect(self.butoneylemi)
        
        self.buton.move(100,20)
        self.plain.move(100,100)
        self.line.move(30,300)
        self.line.resize(450,20)

        self.show()

    def butoneylemi(self):
        if sys.platform == "win32":
            self.linux = ayq.QMessageBox.question(self,"Dur Bakalım","Gnu/Linux kullanmanı tavsiye ederim , göz atarmısın ?",ayq.QMessageBox.Yes | ayq.QMessageBox.No)
            if self.linux == ayq.QMessageBox.Yes:
                webbrowser.open("https://distrowatch.com/")
            else:
                sys.exit("Tüh")
        
        else:
            self.plain.setPlainText("Merhaba , dostum\n\nBu örnek t.me/pngmerkez için oluşturulmuştur .\n\nIstediğin gibi kullanabilir , özelleştirebilirsin ...\n\nHerhangi bir yerde takılırsan ;\nt.me/PngHacking 'e yazman yeterli olur ..")


if __name__ == "__main__":
    uygulama = ayq.QApplication([" "])
    penc = pencere()
    uygulama.exec_()
        

