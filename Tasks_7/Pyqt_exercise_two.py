from PyQt5.QtWidgets import *
from PyQt5 import QtCore
app = QApplication([])
window = QWidget()

label_one = QLabel('label 1')
label_one.setAlignment(QtCore.Qt.AlignCenter)
label_one.setStyleSheet("QLabel{font-size: 12pt;}")

label_two = QLabel('label 2')
label_two.setAlignment(QtCore.Qt.AlignCenter)
label_two.setStyleSheet("QLabel{font-size: 14pt;}")

layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
layout.addWidget(label_one)
layout.addWidget(label_two)


window.setLayout(layout)
window.show()
app.exec()