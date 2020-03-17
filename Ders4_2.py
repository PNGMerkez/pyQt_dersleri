#Bu dersimizde Vertical Box ve Horizontal Box Layout iç içe kullanmayı ele aldım. 
#@ykslkrkci tarafından Persona Non Grata İçin Hazırlanmıştır.
import sys #Gerekli Modülleri içeri Aktardık.
from PyQt5 import QtWidgets #Gerekli Modülleri içeri Aktardık.

def pencere():   #İskeletimizi kurmaya başlıyoruz
    app = QtWidgets.QApplication(sys.argv) #Uygulama objemizi oluşturuyoruz.
    tamam = QtWidgets.QPushButton("Tamam") #Buton oluşturduk.
    çıkıs = QtWidgets.QPushButton("İptal") #Buton oluşturduk.

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch() #Butonlarımız sağ tarafa yaslanıcaklar.
    h_box.addWidget(tamam)
    h_box.addWidget(çıkıs)
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere = QtWidgets.QWidget()    #Pencere Objemizi OLuşturuyoruz.
    pencere.setWindowTitle("Persona Non Grata") #Penceremize Başlık Verdik
    pencere.setLayout(v_box) #Layoutu Penceremize Ekliyoruz.
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_()) 

pencere()  