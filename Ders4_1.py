#Bu dersimizde Vertical Box Layout oluşturmayı ele aldım. @ykslkrkci tarafından Persona Non Grata İçin Hazırlanmıştır.
import sys #Gerekli Modülleri içeri Aktardık.
from PyQt5 import QtWidgets #Gerekli Modülleri içeri Aktardık.

def pencere():   #İskeletimizi kurmaya başlıyoruz
    app = QtWidgets.QApplication(sys.argv) #Uygulama objemizi oluşturuyoruz.
    tamam = QtWidgets.QPushButton("Tamam") #Buton oluşturduk.
    çıkıs = QtWidgets.QPushButton("İptal") #Buton oluşturduk.

    v_box = QtWidgets.QVBoxLayout() #Horizontal Box Layout oluşturduk.
    v_box.addWidget(tamam)
    v_box.addWidget(çıkıs) #Butonlarımızı Vertical Box Layoutlarımıza ekliyoruz.
    v_box.addStretch() #Butonları Yukarı yasladık.
    #v_box.addStretch() kodunu butonları tanımlamadan yazsaydık butonlar aşağı yaslanıcaklardı.
    #v_box.addStretch() butonların ortasına yazarsak butonlardan birisi yukarıda diğeri aşağıda yaslanır.
    pencere = QtWidgets.QWidget()    #Pencere Objemizi OLuşturuyoruz.
    pencere.setWindowTitle("Persona Non Grata") #Penceremize Başlık Verdik
    pencere.setLayout(v_box) #Layoutu Penceremize Ekliyoruz.
    pencere.setGeometry(100,100,500,500)
    
    
    
    
    pencere.show()  #Penceremizi Uygulamamızın İçinde Göstermek İstiyoruz.
    sys.exit(app.exec_()) #Uygulamamızı Sürekli çalışır bir halde olması için döngüye sokuyoruz.Biz X a basmadığımız sürece çalışır durumda bekletiyor.
pencere() #Fonksiyonumuzu Çağırdık.

#Yukarıdaki 9 satır kod bizim kabuğumuz olacaktır, ezberlemenize gerek yok eliniz yavaş yavaş alışıcaktır.(Bir Website için html ne ise bizim içinde o)

