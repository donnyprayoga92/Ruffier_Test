# write here a code for the main app and the first screen
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # memeriksa jenis-jenis nilai input
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

class MainWin(QWidget):
   def __init__(self):
       ''' the window which the greeting is located in '''
       super().__init__()

       # mengatur seperti apa tampilan jendela (label, ukuran, lokasi)
       self.set_appear()

       # membuat dan mengkonfigurasi elemen grafis:
       self.initUI()

       #membuat hubungan antar elemen
       self.connects()

       # Mulai:
       self.show()

   def initUI(self):
       ''' membuat elemen-elemen grafis '''
       self.btn_next = QPushButton(txt_next)
       self.btn_next.setFont(QFont('Times', 15))
       self.hello_text = QLabel(txt_hello)
       self.hello_text.setFont(QFont('Times', 24))
       self.instruction = QLabel(txt_instruction)
       self.instruction.setFont(QFont('Times', 12))

       self.layout = QVBoxLayout()
       self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout)

         
   def next_click(self):
       self.tw = TestWin()
       self.hide()

   def connects(self):
       self.btn_next.clicked.connect(self.next_click)

   ''' mengatur seperti apa tampilan jendela (label, ukuran, lokasi) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

def main():
   app = QApplication([])
   mw = MainWin()
   app.exec_()

main()
