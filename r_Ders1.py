import PyQt5.QtWidgets as ayq # from .. import * 'u önermiyorum !
import sys

# pngmerkez.com | t.me/pngmerkez 'için @raifpy tarafından hazırlanmıştır .
# Bu betikte hem nesne tabanlı hemde normal biçemde pencere oluşturacağız AMA
# Bundan sonraki betiklerde nesne tabanlı olacak . Normal kodlar örnek olması açısından ..

# NON OOP

uygulama = ayq.QApplication(["Sallamasyon_deger:D"]) # sys.argv değeri verilir . Lakin sys.argv'da bu betiğin dosyadını döndürecekti
pencere = ayq.QWidget() # Penceremizi tanımladık


pencere.setWindowTitle("Merhaba Dünya") # pencere başlığını tanımladık
pencere.setGeometry(100,100,500,200) # sol , üst , en , boy
pencere.show() # pencereyi görünür yaptık

uygulama.exec_() # çarpıya basana kadar buradayız
print("Uygulamadan çıkıldı :)") # pencereyi kapattıktan sonra buradan devam ediyoruz

# Normal kodları oldukça basit . Nesne tabanlı da öyle hiç endişe etmeleim ..

class pencere(ayq.QWidget):
    def __init__(self): # __init__'i çaktık hemen :D
        super().__init__() # QWidget'daki yetkileri istediğimiz gibi aktarmak için züper yapısını kullandık
        self.sol = 100 # gemoetry'de vereceğim değerleri hazır ediyoruz
        self.ust = 100 # //
        self.en = 500 #    //
        self.boy = 200  #//
        self.title = "Merhaba Dünya !" # Pencere başlığı değerimizi girdik

        # Girdiğimiz bu değerler bize kolaylık sağlayacak . Girmesek de olurdu ..


        self.komutlar() # komutlar adlı elemanı çağırdık ! (çağırmasak , doğrudan kodları buraya yazsak da olurdu . Hiçbir farkyok)

    def komutlar(self): # pencere adlı elemanı yazdık
        self.setWindowTitle(self.title) #!! setWindowsTitle QWidget elemanı !
        self.setGeometry(self.sol,self.ust,self.en,self.boy) # sol , ust , en , boy
        self.show() # pencere.show() ile aynı eleman 

if __name__ == "__main__": # betiği doğrudan açtıysak True çıktısı ile yola devam 
    uygulama = ayq.QApplication(sys.argv) # içine ['uwurgluckoficiual'] yazsanız bile kabul edecektir
    pencere = pencere() # değere atamak zorundayız . Yoksa elemanı göremeyiz :)
    uygulama.exec_() # Çarpıya basana kadar bu satırı aşamıyoruz | t.me/pngmerkez
    print("Çarpıya basılmış :)")

# Bu betiği doğrudan açarsanız non oop olan kodlar çalışacak , nesne tabanlı olanlar ise "parçalanma arızası" hatası verecektir .

#  Umarım yararı olmuştur . Diğer betiğe devam
