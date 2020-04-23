import PyQt5.QtWidgets as ayq # Default
import sys

class pencere(ayq.QWidget):
    def __init__(self):
        super().__init__()
        self.sol = 200
        self.ust = 300
        self.en = 300
        self.boy = 300
        self.title = "PENCER"

        self.msgbox_title = "UYARI"
        self.msgbox_icerg = "Devam edilsin mi ?"


        self.kodlama()

    def kodlama(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol,self.ust,self.en,self.boy)

        self.uyari = ayq.QMessageBox.question(self,self.msgbox_title,self.msgbox_icerg, ayq.QMessageBox.Yes | ayq.QMessageBox.No ,ayq.QMessageBox.No)
        #self.uyari ile uyari değişkenini oluşturduk . QMessageBox'un soru elemanını kullanıyoruz . ilk değer self , ikincisini title , 3. 'sü messabox'un içeriği , 4 | 5 ise seçenekeler . Sonuncu ise hangi seçeneğin default işaretli olacağını belirtiyoruz .

        if self.uyari == ayq.QMessageBox.No :
            print("Çıkılıyor !")
            sys.exit()

        elif self.uyari == ayq.QMessageBox.Yes :
            print("Devam !")

        # Bu şekilde de Evet | hayır'ı koşullayabiliyoruz .

        # Diğer kutular ve seçenekler sonra ..



        self.show() # self.show() 'u kapatırsanız sadece uyarı kutusu gözükür . ama program çalışmaya devam eder
if __name__ == "__main__":
    appp = ayq.QApplication(sys.argv)
    penc = pencere()
    appp.exec_()