import sys #This module provide access to some variable used or maintained by the intrepreter
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont# untuk font
from PyQt5.QtCore import Qt


# basically function nih kita akan customizekan our window to the user
class MainWindow(QMainWindow):
    def __init__(self):# kene buat constructor
        super().__init__()
        self.setWindowTitle("My Cool first GUI")
#                        x,   y,width,height
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\BELAJAR PHYTON\\ayang comle.jpg"))
        label=QLabel("Hello", self) # nih dia hantar Q label punya constructor hello dan object
        label.setFont(QFont("Arial",30))# kene buat set font dlm set font kene hantar value constructor for QFOnt
        label.setGeometry(0,0,500,100) # untuk adjust label 
        label.setStyleSheet("color:#292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # untuk warna kan 
        
       # label.setAlignment(Qt.AlignTop) # Vertically Top
       # label.setAlignment(Qt.AlignBottom) #Vertically Bottom
       # label.setAlignment(Qt.AlignVCenter) # Vertically center

       # label.setAlignment(Qt.AlignRight) # Horizontal Right
       # label.setAlignment(Qt.AlignHCenter) #Horizontal Center
       # label.setAlignment(Qt.AlignLeft)# Horizontal Left

       # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center and top
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)# Center and Bottom
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)# Center and Center
        
        

def main():
    
    app= QApplication(sys.argv)
    window = MainWindow() 
    window.show()
    sys.exit(app.exec_()) 


if __name__=="__main__":
    main()


