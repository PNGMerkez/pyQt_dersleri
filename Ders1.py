#Bu dersimizde pencere oluşturulmasını ele aldım. @ykslkrkci tarafından Persona Non Grata İçin Hazırlanmıştır.
import sys #Gerekli Modülleri içeri Aktardık.
from PyQt5 import QtWidgets #Gerekli Modülleri içeri Aktardık.

def pencere():   #İskeletimizi kurmaya başlıyoruz
    app = QtWidgets.QApplication(sys.argv) #Uygulama objemizi oluşturuyoruz.
    pencere = QtWidgets.QWidget()    #Pencere Objemizi OLuşturuyoruz.
    pencere.setWindowTitle("Persona Non Grata") #Penceremize Başlık Verdik
    pencere.show()  #Penceremizi Uygulamamızın İçinde Göstermek İstiyoruz.
    sys.exit(app.exec_()) #Uygulamamızı Sürekli çalışır bir halde olması için döngüye sokuyoruz.Biz X a basmadığımız sürece çalışır durumda bekletiyor.
pencere() #Fonksiyonumuzu Çağırdık.

#Yukarıdaki 9 satır kod bizim kabuğumuz olacaktır, ezberlemenize gerek yok eliniz yavaş yavaş alışıcaktır.(Bir Website için html ne ise bizim içinde o)

