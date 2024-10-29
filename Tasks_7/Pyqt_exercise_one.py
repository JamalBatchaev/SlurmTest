from PyQt5.QtWidgets import *
from PyQt5 import QtCore
app = QApplication([])
label = QLabel('Hello World!')
label.setAlignment(QtCore.Qt.AlignCenter)

label.setStyleSheet("QLabel{font-size: 18pt;}")
label.show()
app.exec()