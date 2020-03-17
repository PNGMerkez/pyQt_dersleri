#Bu dersimizde Horizontal Box Layout oluşturmayı ele aldım. @ykslkrkci tarafından Persona Non Grata İçin Hazırlanmıştır.
import sys #Gerekli Modülleri içeri Aktardık.
from PyQt5 import QtWidgets #Gerekli Modülleri içeri Aktardık.

def pencere():   #İskeletimizi kurmaya başlıyoruz
    app = QtWidgets.QApplication(sys.argv) #Uygulama objemizi oluşturuyoruz.
    tamam = QtWidgets.QPushButton("Tamam") #Buton oluşturduk.
    çıkıs = QtWidgets.QPushButton("İptal") #Buton oluşturduk.

    h_box = QtWidgets.QHBoxLayout() #Horizontal Box Layout oluşturduk.
    h_box.addWidget(tamam)
    h_box.addWidget(çıkıs) #Butonlarımızı Horizontal Box Layoutlarımıza ekliyoruz.
    h_box.addStretch() #Butonları Sola Yasladık.Pencereyi Sağ yönde büyütsek bile butonlar solda kalıcak.
    #h_box.addStretch() kodunu butonları tanımlamadan yazsaydık butonlar sağa yaslanıcaklardı.
    #h_box.addStretch() butonların ortasına yazarsak butonlardan birisi sağa diğeri sola yaslanır.
    pencere = QtWidgets.QWidget()    #Pencere Objemizi OLuşturuyoruz.
    pencere.setWindowTitle("Persona Non Grata") #Penceremize Başlık Verdik
    pencere.setLayout(h_box) #Layoutu Penceremize Ekliyoruz.
    pencere.setGeometry(100,100,500,500)
    
    
    
    
    pencere.show()  #Penceremizi Uygulamamızın İçinde Göstermek İstiyoruz.
    sys.exit(app.exec_()) #Uygulamamızı Sürekli çalışır bir halde olması için döngüye sokuyoruz.Biz X a basmadığımız sürece çalışır durumda bekletiyor.
pencere() #Fonksiyonumuzu Çağırdık.

#Yukarıdaki 9 satır kod bizim kabuğumuz olacaktır, ezberlemenize gerek yok eliniz yavaş yavaş alışıcaktır.(Bir Website için html ne ise bizim içinde o)

