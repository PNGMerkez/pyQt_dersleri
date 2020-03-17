#Bu dersimizde buton oluşturulmasını ele aldım. @ykslkrkci tarafından Persona Non Grata İçin Hazırlanmıştır.
import sys #Gerekli Modülleri içeri Aktardık.
from PyQt5 import QtWidgets #Gerekli Modülleri içeri Aktardık.

def pencere():   #İskeletimizi kurmaya başlıyoruz
    app = QtWidgets.QApplication(sys.argv) #Uygulama objemizi oluşturuyoruz.

    pencere = QtWidgets.QWidget()    #Pencere Objemizi OLuşturuyoruz.
    pencere.setWindowTitle("Persona Non Grata") #Penceremize Başlık Verdik

    button = QtWidgets.QPushButton(pencere) #Nutonumuzu Penceremize Ekledik
    button.setText("İlk Butonumuz")   #Butonumuza İsim Verdik.
    yazı = QtWidgets.QLabel(pencere)  #Etiket OLuşturduk.
    yazı.setText("Merhaba Persona Non Grata") #Yazımızı İsimlendirdik.

    button.move(150,150) #Butonumuzun Konumunu Ayarladık
    yazı.move(130,50)    #Etiketimizin Konumunu Ayarladık.
 
    pencere.setGeometry(150,150,400,400)
    pencere.show()  #Penceremizi Uygulamamızın İçinde Göstermek İstiyoruz.
    sys.exit(app.exec_()) #Uygulamamızı Sürekli çalışır bir halde olması için döngüye sokuyoruz.Biz X a basmadığımız sürece çalışır durumda bekletiyor.
pencere() #Fonksiyonumuzu Çağırdık.

