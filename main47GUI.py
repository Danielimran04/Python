import sys #This module provide access to some variable used or maintained by the intrepreter
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt5.QtGui import QIcon

#QApplication Dia adalah “otak utama” atau pengurus aplikasi.Tugas dia: uruskan event loop (klik, taip, gerakkan mouse, resize window, dll).
# Tanpa QApplication, window kau memang tak boleh hidup — walaupun kau dah buat QMainWindow.

# basically function nih kita akan customizekan our window to the user
class MainWindow(QMainWindow):
    def __init__(self):# kene buat constructor
        super().__init__()
        self.setWindowTitle("My Cool first GUI")
#                        x,   y,width,height
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\BELAJAR PHYTON\\ayang comle.jpg"))
        

def main():
    #QApplication(...) Membuat satu instance aplikasi.Cuma boleh ada SATU QApplication dalam satu program (kalau lebih, PyQt akan error).
    app= QApplication(sys.argv)#  sys.args=Ini hantar “command-line arguments” ke QApplication. Biasanya untuk set style/theme atau config lain kalau kita jalankan program dari terminal.kalau tak perlu letak kosong iaitu []
    window = MainWindow() # call constructor c
    window.show()
    sys.exit(app.exec_()) 


if __name__=="__main__":
    main()


#Apa jadi selepas buat QApplication?
#Kau buat window (MainWindow).
#Kau panggil window.show().
#Kemudian kau start event loop dengan:
#sys.exit(app.exec_())
#exec_() inilah yang menjaga program sentiasa hidup sampai user tutup tingkap.

#untuk line 9
#QMainWindow → sudah ada constructor (__init__) dalam dia yang uruskan semua setup asas untuk sebuah window (contohnya: bingkai tingkap, bar tajuk, event handler, menu bar, status bar, dll).
#Bila kau panggil super().__init__() → kau aktifkan constructor QMainWindow dulu supaya semua fungsi asas tingkap siap sedia.
#Lepas tu barulah kau boleh tambah customization sendiri (contoh setWindowTitle, setGeometry, dll).