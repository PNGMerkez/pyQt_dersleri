#Bu dersimizde pencereye yazı ve resim eklenmesini ele aldım. @ykslkrkci tarafından Persona Non Grata İçin Hazırlanmıştır.
import sys  #Gerekli Modülleri içeri Aktardık.
from PyQt5 import QtWidgets, QtGui #Modülleri İçeri Aktardım.

def pencere():   #İskeletimizi kurmaya başlıyoruz.
    app = QtWidgets.QApplication(sys.argv) #Uygulama objemizi oluşturuyoruz.
    pencere = QtWidgets.QWidget()    #Pencere Objemizi OLuşturuyoruz.
    pencere.setWindowTitle("Persona Non Grata") #Penceremize Başlık Verdik
    etiket = QtWidgets.QLabel(pencere) #Etiketimi Pencere Üzerine Yapıştırdım.
    etiket.setPixmap(QtGui.QPixmap("Resim.png")) #İşlem yaptığınız dizinde resim bulunmalı.
    yazım1 = QtWidgets.QLabel(pencere) #Etiketimi Pencere Üzerine Yapıştırdım.
    yazım1.setText("Deneme1") #Etiketimde ne yazıcağını ayarladım.
    yazım1.move(200,30) #Etiketimi Taşıdım.
    etiket.move(200,70) #Etiketimi Taşıdım.
    pencere.setGeometry(100,100,500,500) #100 100 değerimiz masaüstünde nereden başlıyacağını belirtiyoruz.(Sol Yukarı) 500 500'de Penceremizin Büyüklüğünü ayarlamış oluyoruz.
    pencere.show()  #Penceremizi Uygulamamızın İçinde Göstermek İstiyoruz.
    sys.exit(app.exec_()) #Uygulamamızı Sürekli çalışır bir halde olması için döngüye sokuyoruz.Biz X a basmadığımız sürece çalışır durumda bekletiyor.
pencere() #Fonksiyonumuzu Çağırdık.
